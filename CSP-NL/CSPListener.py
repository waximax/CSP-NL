# Generated from CSP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSPParser import CSPParser
else:
    from CSPParser import CSPParser

# This class defines a complete listener for a parse tree produced by CSPParser.
class CSPListener(ParseTreeListener):

    # Enter a parse tree produced by CSPParser#cspFile.
    def enterCspFile(self, ctx:CSPParser.CspFileContext):
        pass

    # Exit a parse tree produced by CSPParser#cspFile.
    def exitCspFile(self, ctx:CSPParser.CspFileContext):
        pass


    # Enter a parse tree produced by CSPParser#processDefinition.
    def enterProcessDefinition(self, ctx:CSPParser.ProcessDefinitionContext):
        pass

    # Exit a parse tree produced by CSPParser#processDefinition.
    def exitProcessDefinition(self, ctx:CSPParser.ProcessDefinitionContext):
        pass


    # Enter a parse tree produced by CSPParser#channelDefinition.
    def enterChannelDefinition(self, ctx:CSPParser.ChannelDefinitionContext):
        pass

    # Exit a parse tree produced by CSPParser#channelDefinition.
    def exitChannelDefinition(self, ctx:CSPParser.ChannelDefinitionContext):
        pass


    # Enter a parse tree produced by CSPParser#assertion.
    def enterAssertion(self, ctx:CSPParser.AssertionContext):
        pass

    # Exit a parse tree produced by CSPParser#assertion.
    def exitAssertion(self, ctx:CSPParser.AssertionContext):
        pass


    # Enter a parse tree produced by CSPParser#assertionType.
    def enterAssertionType(self, ctx:CSPParser.AssertionTypeContext):
        pass

    # Exit a parse tree produced by CSPParser#assertionType.
    def exitAssertionType(self, ctx:CSPParser.AssertionTypeContext):
        pass


    # Enter a parse tree produced by CSPParser#assertionModel.
    def enterAssertionModel(self, ctx:CSPParser.AssertionModelContext):
        pass

    # Exit a parse tree produced by CSPParser#assertionModel.
    def exitAssertionModel(self, ctx:CSPParser.AssertionModelContext):
        pass


    # Enter a parse tree produced by CSPParser#trace.
    def enterTrace(self, ctx:CSPParser.TraceContext):
        pass

    # Exit a parse tree produced by CSPParser#trace.
    def exitTrace(self, ctx:CSPParser.TraceContext):
        pass


    # Enter a parse tree produced by CSPParser#parameters.
    def enterParameters(self, ctx:CSPParser.ParametersContext):
        pass

    # Exit a parse tree produced by CSPParser#parameters.
    def exitParameters(self, ctx:CSPParser.ParametersContext):
        pass


    # Enter a parse tree produced by CSPParser#expression.
    def enterExpression(self, ctx:CSPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#expression.
    def exitExpression(self, ctx:CSPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#prefixExpression.
    def enterPrefixExpression(self, ctx:CSPParser.PrefixExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#prefixExpression.
    def exitPrefixExpression(self, ctx:CSPParser.PrefixExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#inputPatternExpression.
    def enterInputPatternExpression(self, ctx:CSPParser.InputPatternExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#inputPatternExpression.
    def exitInputPatternExpression(self, ctx:CSPParser.InputPatternExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#restrictedInputExpression.
    def enterRestrictedInputExpression(self, ctx:CSPParser.RestrictedInputExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#restrictedInputExpression.
    def exitRestrictedInputExpression(self, ctx:CSPParser.RestrictedInputExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#nondeterministicRestrictedInputExpression.
    def enterNondeterministicRestrictedInputExpression(self, ctx:CSPParser.NondeterministicRestrictedInputExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#nondeterministicRestrictedInputExpression.
    def exitNondeterministicRestrictedInputExpression(self, ctx:CSPParser.NondeterministicRestrictedInputExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#outputExpression.
    def enterOutputExpression(self, ctx:CSPParser.OutputExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#outputExpression.
    def exitOutputExpression(self, ctx:CSPParser.OutputExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#nondeterministicInputExpression.
    def enterNondeterministicInputExpression(self, ctx:CSPParser.NondeterministicInputExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#nondeterministicInputExpression.
    def exitNondeterministicInputExpression(self, ctx:CSPParser.NondeterministicInputExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#baseExpression.
    def enterBaseExpression(self, ctx:CSPParser.BaseExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#baseExpression.
    def exitBaseExpression(self, ctx:CSPParser.BaseExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#eventList.
    def enterEventList(self, ctx:CSPParser.EventListContext):
        pass

    # Exit a parse tree produced by CSPParser#eventList.
    def exitEventList(self, ctx:CSPParser.EventListContext):
        pass


    # Enter a parse tree produced by CSPParser#event.
    def enterEvent(self, ctx:CSPParser.EventContext):
        pass

    # Exit a parse tree produced by CSPParser#event.
    def exitEvent(self, ctx:CSPParser.EventContext):
        pass



del CSPParser