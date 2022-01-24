const {parse} = require('/graphql/language/parser');
const { visit } = require('/graphql/language/visitor');
const { print } = require('/graphql/language/printer');

function callGraphQlParse(graphQlQueryStr) {
    const queryDocumentAst = parse(graphQlQueryStr);
    console.log("Begin AST");
    console.log(queryDocumentAst);
    console.log("End AST");
    console.log(print(queryDocumentAst));
    console.log("Post AST");

    const editedAST = visit(queryDocumentAst, {
        enter(node, key, parent, path, ancestors) {
            console.log("node");
            console.log(JSON.stringify(node));
        },
        leave(node, key, parent, path, ancestors) {
        }
    });

    return JSON.stringify(queryDocumentAst);
}

exports.callGraphQlParse = callGraphQlParse;