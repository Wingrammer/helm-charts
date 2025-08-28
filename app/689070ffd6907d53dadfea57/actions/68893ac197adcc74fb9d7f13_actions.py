

from typing import Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

from .actions import KauzaApiCallAction


class demander_articles_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '689a01216b7d9cdb9b5407d3', 'name': 'demander_articles_action', 'send_domain': True, 'intent': 'demander_articles', 'active_loop': '', 'condition': '[]', 'action_type': 'KauzaApiCallAction', 'curl_template': 'curl -H \'Content-Type: application/json\' -X POST -d \'{"article_name":"{{article_slot}}","variants_articles":"{{variants_article_slot}}"}\' \'https://jvendeur-cjbta3hebre2h4e3.canadacentral-01.azurewebsites.net/\'', 'response': 'None', 'responses': '[{\'template\': \'utter_demander_articles\', \'json_message\': \'{"interactive": {"type": "list", "body": {"text": "Voici une liste des articles disponibles. Cliquez sur l’un pour plus d’informations :"}, "action": {"button": "Articles", "sections": [{"title": "Articles", "rows": [{% for article in response %}{"id": "/article_details{{ \\\'{{\\\\"article_id\\\\":\\\\"\\\' + article[\\\'id\\\'] + \\\'\\\\"}}\\\' }}","title": "{{ article[\\\'name\\\'] }}"}{% if not loop.last %},{% endif %}{% endfor %}] }]}}}\'}]', 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '68893ac197adcc74fb9d7f13'}

    def name(self) -> Text:
        return "demander_articles_action"

class article_details_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '5eb7cf5a86d9755df3a6c593', 'name': 'article_details_action', 'send_domain': True, 'intent': 'None', 'active_loop': 'string', 'condition': '[{}]', 'action_type': 'KauzaApiCallAction', 'curl_template': "curl -H 'Content-Type: application/json' -X GET 'https://jvendeur-cjbta3hebre2h4e3.canadacentral-01.azurewebsites.net/{{article_id}}'", 'response': '{}', 'responses': "[{'template': 'utter_article_details', 'text': 'Voici les détails de ce article :\\n - Montant: {invoice_amount}\\n - Nom du client: {client_name}\\n - Email du client: {client_email}\\n - Adresse de la boutique : {client_address}\\n - Numéro de téléphone du client: {client_phone_number}\\n - Description: {invoice_description}\\n - Boutique: {invoice_store}', 'image': '{{article_image}}'}]", 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '68893ac197adcc74fb9d7f13'}

    def name(self) -> Text:
        return "article_details_action"

class paiement_effectué_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '689a05386b7d9cdb9b5407da', 'name': 'paiement_effectué_action', 'send_domain': True, 'intent': 'paiement_effectué', 'active_loop': '', 'condition': '[]', 'action_type': 'KauzaApiCallAction', 'curl_template': "curl -H 'Content-Type: application/json' -X GET 'https://event-api-iwgk.vercel.app/events?reference=%7B%7Breference_paiement_slot%7D%7D'", 'response': 'None', 'responses': '[{\'template\': \'utter_paiement_effectué\', \'text\': "Si le paiement est effectué, il aura tel message. Et si ca n\'a pas été valider, il aura un autre"}]', 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '68893ac197adcc74fb9d7f13'}

    def name(self) -> Text:
        return "paiement_effectué_action"
