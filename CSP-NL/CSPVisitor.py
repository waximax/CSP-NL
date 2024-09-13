# Generated from CSP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSPParser import CSPParser
else:
    from CSPParser import CSPParser

# This class defines a complete generic visitor for a parse tree produced by CSPParser.

class CSPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSPParser#cspFile.
    def visitCspFile(self, ctx:CSPParser.CspFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#processDefinition.
    def visitProcessDefinition(self, ctx:CSPParser.ProcessDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#channelDefinition.
    def visitChannelDefinition(self, ctx:CSPParser.ChannelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#assertion.
    def visitAssertion(self, ctx:CSPParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#assertionType.
    def visitAssertionType(self, ctx:CSPParser.AssertionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#assertionModel.
    def visitAssertionModel(self, ctx:CSPParser.AssertionModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#trace.
    def visitTrace(self, ctx:CSPParser.TraceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#parameters.
    def visitParameters(self, ctx:CSPParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#expression.
    def visitExpression(self, ctx:CSPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#prefixExpression.
    def visitPrefixExpression(self, ctx:CSPParser.PrefixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#inputPatternExpression.
    def visitInputPatternExpression(self, ctx:CSPParser.InputPatternExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#restrictedInputExpression.
    def visitRestrictedInputExpression(self, ctx:CSPParser.RestrictedInputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#nondeterministicRestrictedInputExpression.
    def visitNondeterministicRestrictedInputExpression(self, ctx:CSPParser.NondeterministicRestrictedInputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#outputExpression.
    def visitOutputExpression(self, ctx:CSPParser.OutputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#nondeterministicInputExpression.
    def visitNondeterministicInputExpression(self, ctx:CSPParser.NondeterministicInputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#baseExpression.
    def visitBaseExpression(self, ctx:CSPParser.BaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#eventList.
    def visitEventList(self, ctx:CSPParser.EventListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#event.
    def visitEvent(self, ctx:CSPParser.EventContext):
        return self.visitChildren(ctx)



del CSPParser