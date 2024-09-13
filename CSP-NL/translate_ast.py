import sys
from antlr4 import *
from CSPParser import CSPParser
from CSPLexer import CSPLexer
from CSPVisitor import CSPVisitor

class CSPToASTVisitor(CSPVisitor):
    def visitChannelDefinition(self, ctx: CSPParser.ChannelDefinitionContext):
        channels_with_range = []
        channels_without_range = []

        for i in range(len(ctx.ID())):
            channel_name = ctx.ID(i).getText()
            if ctx.getChildCount() > 1 and ctx.INT(0):
                range_values = ctx.INT(0).getText()
                if ctx.INT(1):
                    range_values += f"..{ctx.INT(1).getText()}"
                channels_with_range.append(f"{channel_name} declared with range {{{range_values}}}.")
            else:
                channels_without_range.append(channel_name)
        
        # Output channels with range
        for channel_with_range in channels_with_range:
            print(f"Channel {channel_with_range}")
        
        # Output channels without range
        if channels_without_range:
            print(f"The following communication channels are set up: {', '.join(channels_without_range)}.")
        
        return None



    def visitProcessDefinition(self, ctx: CSPParser.ProcessDefinitionContext):
        process_name = ctx.ID().getText()
        print(f"Defining process {process_name}.")
        expression = ctx.expression()
        explanation = self.visit(expression)
        # 移除多余的句号
        explanation = explanation.rstrip('.')
        print(f"{process_name} does the following: {explanation}.")
        return None


    def visitAssertion(self, ctx: CSPParser.AssertionContext):
        process_name = ctx.ID().getText()
        assertion_type = self.visit(ctx.assertionType())
        result = f"This assertion checks whether the process {process_name} {assertion_type if assertion_type else 'could not interpret this check.'}"
        print(result)
        return result

    def visitAssertionType(self, ctx: CSPParser.AssertionTypeContext):
        assertion_text = ctx.getText()

        if '[has trace]' in assertion_text:
            trace = self.visit(ctx.trace())
            trace_description = ", ".join([event for event in trace.strip('<>').split(', ')])
            if ',' in trace:
                return f"can perform the sequence of events {trace_description.replace(', ', ' followed by ')}."
            else:
                return f"can perform the event {trace_description}."
        elif 'deadlock free' in assertion_text:
            return "must never reach a state where no further actions are possible (deadlock-free)."
        elif 'divergence free' in assertion_text:
            return "should not enter an endless loop (no divergence)."
        elif 'deterministic' in assertion_text:
            return "should behave predictably (deterministic)."
        elif '[T=' in assertion_text or '[F=' in assertion_text or '[FD=' in assertion_text:
            model = assertion_text.split('[')[1].split('=')[0]
            return f"is checked for correctness under the {model} model."
        else:
            return None


    def visitTrace(self, ctx: CSPParser.TraceContext):
        events = [self.visit(event) for event in ctx.event()]
        return f"<{', '.join(events)}>"

    def visitEvent(self, ctx: CSPParser.EventContext):
        return ctx.getText()

    def visitBaseExpression(self, ctx: CSPParser.BaseExpressionContext):
        if ctx.STOP_RULE():
            return "STOP (the process ends here)."
        elif ctx.SKIP_RULE():
            return "SKIP (indicating successful completion)."
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None


    def visitExpression(self, ctx: CSPParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            operator = ctx.getChild(1).getText()
            if operator == '[]':
                process1_description = self.visit(ctx.getChild(0))
                process2_description = self.visit(ctx.getChild(2))
                return (f"The process offers an external choice: it can either {process1_description.strip('.')}, "
                        f"or {process2_description.strip('.')}, depending on the environment.")
            elif operator == '|||':
                process1 = self.visit(ctx.getChild(0))
                process2 = self.visit(ctx.getChild(2))
                return (f"The processes {process1.strip()} and {process2.strip()} are interleaved, "
                        f"meaning they run in parallel without any synchronization. "
                        f"This is equivalent to {process1.strip()} [| {{}} |] {process2.strip()}.")
            elif operator == ';':
                process1 = self.visit(ctx.getChild(0))
                process2 = self.visit(ctx.getChild(2))
                return (f"The process {process1.strip()} runs first. Once it terminates (turns into SKIP), "
                        f"the process {process2.strip()} will begin execution.")
            elif operator == '&':
                condition = ctx.getChild(0).getText()
                process = self.visit(ctx.getChild(2))
                if condition == "true":
                    return (f"If the condition is true, the process behaves as follows: {process.strip('.')}.")
                else:
                    return (f"If the condition is false, the process behaves as STOP (the process ends here).")
        elif ctx.getChildCount() == 11:
            process1_name = ctx.getChild(0).getText()
            process2_name = ctx.getChild(10).getText()
            events1 = "{" + ctx.getChild(3).getText() + "}"
            events2 = "{" + ctx.getChild(7).getText() + "}"
            return (f"Process {process1_name} and Process {process2_name} must synchronize on the intersection "
                    f"of the event sets {events1} and {events2}. If there is no intersection between {events1} and {events2}, "
                    f"then {process1_name} and {process2_name} can execute in parallel without requiring synchronization.")
        elif ctx.getChildCount() == 7:
            process1 = self.visit(ctx.getChild(0))
            process2 = self.visit(ctx.getChild(6))
            events = "{" + ctx.getChild(3).getText() + "}"
            return (f"The processes {process1.strip()} and {process2.strip()} run in parallel, "
                    f"and must synchronize on events in the set {events}. "
                    f"Any event not in {events} may be performed independently by either process.")
        return self.visitChildren(ctx)


    def visitPrefixExpression(self, ctx: CSPParser.PrefixExpressionContext):
        event = ctx.event().getText()
        process = self.visit(ctx.expression())

        # Check if the following process is STOP or SKIP, and if so, generate a simplified description
        if process == "STOP (the process ends here)." or process == "STOP":
            return f"The process performs the {event} event, and then terminates at the stop state."
        elif process == "SKIP (indicating successful completion)." or process == "SKIP":
            return f"The process performs the {event} event, and then transitions to SKIP (indicating successful completion)."
        else:
            return f"The process performs the {event} event, followed by {process[12:].lower()}."






    def visitInputPatternExpression(self, ctx: CSPParser.InputPatternExpressionContext):
        channel = ctx.ID(0).getText()
        pattern = ctx.ID(1).getText()
        process = self.visit(ctx.expression())
        return (f"This is a standard input process that accepts any value (the value is bound to variable {pattern}) "
                f"from channel {channel} without any restrictions using External Choice, and then transitions to  {process}")

    def visitRestrictedInputExpression(self, ctx: CSPParser.RestrictedInputExpressionContext):
        channel = ctx.ID(0).getText()
        pattern = ctx.ID(1).getText()
        values = [ctx.INT(i).getText() for i in range(len(ctx.INT()))]
        process = self.visit(ctx.expression())
        return (f"This is used when you want to restrict the input to specific values, ensuring the process only handles "
                f"certain inputs using External Choice. This process waits to receive a value from channel {channel}, "
                f"but the value must be either {', '.join(values)}, and then transitions to  {process}")

    def visitOutputExpression(self, ctx: CSPParser.OutputExpressionContext):
        channel = ctx.ID().getText()
        value = ctx.INT().getText()
        process = self.visit(ctx.expression())
        return (f"This process sends the value {value} to channel {channel}, and then it performs SKIP, indicating that the process ends.")

    def visitNondeterministicInputExpression(self, ctx: CSPParser.NondeterministicInputExpressionContext):
        channel = ctx.ID(0).getText()
        pattern = ctx.ID(1).getText()
        process = self.visit(ctx.expression())
        return (f"This is a standard input process that accepts any value (the value is bound to variable {pattern}) "
                f"from channel {channel} without any restrictions using Internal Choice, and then transitions to  {process}")

    def visitNondeterministicRestrictedInputExpression(self, ctx: CSPParser.NondeterministicRestrictedInputExpressionContext):
        channel = ctx.ID(0).getText()
        pattern = ctx.ID(1).getText()
        values = [ctx.INT(i).getText() for i in range(len(ctx.INT()))]
        process = self.visit(ctx.expression())
        return (f"This is used when you want to restrict the input to specific values, ensuring the process only handles "
                f"certain inputs using Internal Choice. This process waits to receive a value from channel {channel}, "
                f"but the value must be either {', '.join(values)}, and then transitions to  {process}")


def main(argv):
    if len(argv) < 2:
        print("Usage: python translate_ast.py <input_file.csp>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = CSPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSPParser(stream)
    tree = parser.cspFile()

    visitor = CSPToASTVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
