const { NerManager } = require('node-nlp');

const manager = new NerManager({ threshold: 0.8 });
manager.addNamedEntityText(
    'pain',
    'head ache',
    ['en'],
    ['head ache', 'head ache'],
);
manager.addNamedEntityText(
    'pain',
    'throat pain',
    ['en'],
    ['throat pain', 'throat pain'],
);
manager.addNamedEntityText('anxiety', 'sleeplessness', ['en'], ['anxiety']);
manager.addNamedEntityText(
    'pain',
    'body pain',
    ['en'],
    ['body pain', 'body pain'],
);
manager.addNamedEntityText('pain', 'chest pain', ['en'], ['chest pain']);
//manager.addNamedEntityText('food', 'pasta', ['en'], ['Pasta', 'spaghetti']);
const entity = manager.addNamedEntity('email', 'regex');
entity.addRegex('en', /\b(\w[-._\w]*\w@\w[-._\w]*\w\.\w{2,3})\b/gi);
manager.findEntities(
    'I have body pain and head ache and my throat hurts ',
    'en',
).then(entities => console.log(entities));