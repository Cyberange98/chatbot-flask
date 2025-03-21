from flask import Flask, request, jsonify, Response
import json
import os

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
    }
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    question = data.get("message", "").lower()

    for pierre, details in lithotherapie_data.items():
        if pierre in question:
            response = {
                "pierre": pierre.capitalize(),
                "description": details["description"],
                "utilisation": details["utilisation"],
                "chakra": details["chakra"],
                "signe": details["signe"],
                "entretien": details["entretien"]
            }
            return Response(
                json.dumps(response, ensure_ascii=False),  # ✅ Garder les accents
                content_type="application/json; charset=utf-8"
            )

    return jsonify({"response": "Je ne connais pas encore cette pierre, mais je peux te renseigner sur d'autres. Demande-moi par exemple les bienfaits de l'améthyste ou comment recharger la tourmaline noire."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)



   
