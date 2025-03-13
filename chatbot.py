from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

# Base de connaissances sur les pierres et leurs propriétés
lithotherapie_data = {
    "améthyste": {
        "description": "Pierre apaisante, elle favorise la relaxation et améliore le sommeil.",
        "utilisation": "Utilisée en bijoux, en méditation ou placée dans une chambre.",
        "chakra": "Chakra coronal (7e).",
        "signe": "Poissons, Vierge, Sagittaire.",
        "entretien": "Purification : Eau, encens. Rechargement : Pleine lune, géode d’améthyste."
    },
    "quartz rose": {
        "description": "Pierre de l’amour et de la paix intérieure.",
        "utilisation": "Bijoux, méditation, harmonisation des relations.",
        "chakra": "Chakra du cœur (4e).",
        "signe": "Taureau, Balance.",
        "entretien": "Purification : Eau. Rechargement : Lumière lunaire."
    },
    "tourmaline noire": {
        "description": "Pierre de protection contre les énergies négatives.",
        "utilisation": "Bijoux, placée près des entrées ou du lit.",
        "chakra": "Chakra racine (1er).",
        "signe": "Capricorne.",
        "entretien": "Purification : Eau, sel. Rechargement : Lumière solaire, amas de quartz."
    },
    "citrine": {
        "description": "Pierre d’abondance et de dynamisme, stimule la créativité.",
        "utilisation": "Bijoux, porte-monnaie, méditation.",
        "chakra": "Chakra du plexus solaire (3e).",
        "signe": "Lion, Gémeaux.",
        "entretien": "Purification : Eau. Rechargement : Soleil, amas de quartz."
    },
    "jaspe rouge": {
        "description": "Pierre d’ancrage et de vitalité, favorise la confiance en soi.",
        "utilisation": "Bijoux, méditation, décoration.",
        "chakra": "Chakra racine (1er).",
        "signe": "Bélier, Scorpion.",
        "entretien": "Purification : Eau, terre. Rechargement : Soleil."
    },
    "hématite": {
        "description": "Pierre de force et de protection, absorbe les mauvaises énergies.",
        "utilisation": "Bijoux, pierre roulée dans la poche.",
        "chakra": "Chakra racine (1er).",
        "signe": "Bélier, Scorpion.",
        "entretien": "Purification : Pas d’eau ! Encens, sel sec. Rechargement : Soleil, géode de quartz."
    },
    "onyx": {
        "description": "Pierre d’ancrage et de stabilité émotionnelle.",
        "utilisation": "Bijoux, méditation, protection.",
        "chakra": "Chakra racine (1er).",
        "signe": "Capricorne, Lion.",
        "entretien": "Purification : Eau, encens. Rechargement : Soleil."
    },
    "cristal de roche": {
        "description": "Amplificateur d’énergie, purifie et harmonise.",
        "utilisation": "Utilisé avec d’autres pierres, en méditation.",
        "chakra": "Tous les chakras.",
        "signe": "Tous les signes.",
        "entretien": "Purification : Eau. Rechargement : Soleil, lune."
    },
    "aventurine": {
        "description": "Pierre de chance et d’optimisme.",
        "utilisation": "Bijoux, porte-bonheur, méditation.",
        "chakra": "Chakra du cœur (4e).",
        "signe": "Taureau, Balance.",
        "entretien": "Purification : Eau. Rechargement : Soleil, géode de quartz."
    }
}


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    question = data.get("message", "").lower()
    
    for pierre, details in lithotherapie_data.items():
        if pierre in question:
            response = f"🌿 **{pierre.capitalize()}**\n"
            response += f"✨ {details['description']}\n\n"
            response += f"🛠 **Utilisation** : {details['utilisation']}\n"
            response += f"🌀 **Chakra** : {details['chakra']}\n"
            response += f"♉ **Signes astrologiques** : {details['signe']}\n"
            response += f"💧 **Entretien** : {details['entretien']}\n"
            
            return Response(
                json.dumps({"response": response}, ensure_ascii=False),
                content_type="application/json; charset=utf-8"
            )

    return jsonify({"response": "Je ne connais pas encore cette pierre, mais je peux te renseigner sur d'autres. Demande-moi par exemple les bienfaits de l'améthyste ou comment recharger la tourmaline noire."})
if __name__ == '__main__':
    app.run(debug=True)

   
