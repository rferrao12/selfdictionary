from flask import Flask, jsonify
from flask import abort
from flask import request



app = Flask(__name__)
mdt= [
    {
        'Id':0,
        'Word': u'Corpulent',
        'meaning': u'Obese, having a large bulky body',
        'use in a sentence':u'He had bow-legs and was corpulent'
    },
    {
        'Id':1,
        'Word': u'Allusion',
        'meaning': u'the act of making an indirect reference to something',
        'use in a sentence':u'He made some allusion to the years they lived apart',
    },
    {
        'Id':2,
        'Word': u'Embezzle',
        'meaning': u'to secretly take money that is in your care or that belongs to an organization or business you work for',
        'use in a sentence': u'He embezzled thousands of dollars from the charity.',
    },
    {
        'Id': 3,
        'Word': u'Inebriate',
        'meaning': u'someone who has drunk too much alcohol or who regularly does this',
        'use in a sentence': u'Her husband was a chronic inebriate.',
    },
    {
        'Id': 4,
        'Word': u'Abject',
        'meaning': u'the state of being extremely unhappy, poor, unsuccessful, etc.',
        'use in a sentence': u'This policy has turned out to be an abject failure.',
    },
    {
        'Id': 5,
        'Word': u'Extricate',
        'meaning': u'to remove something or set something free with difficulty',
        'use in a sentence':u'I tried to extricate myself from the situation.',
    },
    {
        'Id': 6,
        'Word': u'Repeal',
        'meaning': u'the act of removing the legal force of a law',
        'use in a sentence':u'Twenty nine senators said they opposed repeal of the death penalty.',
    },
    {
        'Id': 7,
        'Word': u'Diligent',
        'meaning': u'careful and using a lot of effort',
        'use in a sentence': u'Leo is very diligent in/about his work.',
    },
    {
        'Id': 8,
        'Word': u'Deify',
        'meaning': u'to consider someone or something to be so important that they are almost like a god',
        'use in a sentence': u'Lata Mangeshkar was deified by her fans.',
    },
    {
         'Id': 9,
        'Word': u'Cantankerous',
        'meaning': u'arguing and complaining a lot',
        'use in a sentence': u'He is getting a bit cantankerous in his old age.',
    },
    {
         'Id': 10,
        'Word': u'Ken',
        'meaning': u'not in your area of knowledge',
        'use in a sentence': u'Financial matters are beyond my ken, I am afraid',
    },
]
@app.route('/')
def index():
    return "WELCOME TO THE MINI-DICTIONARY"

@app.route('/mdt',methods=['GET'])
def get_w():
    return jsonify({'minidictionary':mdt})

@app.route('/mdt/<string:word_n>', methods=['GET'])
def mean(word_n):
    wd = [wd for wd in mdt if wd['Word'] == word_n]
    return jsonify({'Searched Word': wd[0]})

@app.route('/mdt/sort',methods=['GET'])
def srt():
    s=sorted(mdt, key = lambda i: (i['Word']))
    return jsonify({'Sorted':s})

@app.route('/mdt', methods=['POST'])
def create_w():

    if not request.json or not 'Word' in request.json:
        abort(400)
    md = {
        'Id': mdt[-1]['Id']+1,
        'Word': request.json['Word'],
        'meaning':request.json.get('meaning',""),
        'use in a sentence':request.json.get('use in a sentence',""),
    }
    mdt.append(md)
    return jsonify({'New': md}), 201

@app.route('/mdt/<int:id_w>',methods=['PUT'])
def m_update(id_w):
    #mdt[id_w]['use in a sentence']=" It happened so quick that I had no time to ponder."
    #return jsonify({'up':mdt[id_w]})
    md = [md for md in mdt if md['Id'] == id_w]
    md[0]['Word'] = request.json.get('Word', md[0]['Word'])
    md[0]['meaning'] = request.json.get('meaning', md[0]['meaning'])
    md[0]['use in a sentence'] = request.json.get('use in a sentence', md[0]['use in a sentence'])
    return jsonify({'upword': md[0]})




if __name__ == '__main__':
    app.run(debug=True)
