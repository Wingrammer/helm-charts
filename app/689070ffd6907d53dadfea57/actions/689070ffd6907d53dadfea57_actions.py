























from typing import Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

from .actions import KauzaApiCallAction






class authentification_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a11986ad57daa5de6ad89f', 'name': 'authentification_action', 'send_domain': True, 'intent': 'string', 'active_loop': 'string', 'condition': '[{}]', 'action_type': 'KauzaApiCallAction', 'curl_template': 'curl -H \'Authorization: Basic a2F1emE6a2F1emFhZnJpY2E=\' -H \'Content-Type: application/json\' -X POST -d \'{"email": "{{client_email_slot}}", "telephone": "{{client_phone_number_slot}}"}\' \'https://api-kauzapay.onrender.com/auth/connexion\'', 'response': '{}', 'responses': '[]', 'events': '[{\'event\': \'slot\', \'name\': \'access_token_slot\', \'value\': \'{{access_token}}\'}, {\'event\': \'slot\', \'name\': \'user_id_slot\', \'value\': "{{user[\'id\']}}"}]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "authentification_action"









class invoice_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a11bf4ad57daa5de6ad8a0', 'name': 'invoice_action', 'send_domain': True, 'intent': 'string', 'active_loop': 'string', 'condition': '[{}]', 'action_type': 'KauzaApiCallAction', 'curl_template': 'curl -H \'Content-Type: application/json\' -H \'Authorization: Bearer {{access_token_slot}}\' -X POST -d \'{"phone_number": "{{debtor_phone_number_slot}}", "amount": "{{invoice_amount_slot}}", "description": "{{invoice_description_slot}}", "network": "TMONEY", "email": "{{debtor_email_slot}}"}\' \'https://api-kauzapay.onrender.com/factures/\'', 'response': '{}', 'responses': "[{'template': 'utter_invoice_submit', 'text': 'Votre facture a bien été envoyé au numéro {{debtor_phone_number_slot}}.'}]", 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "invoice_action"








class invoices_list_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a11cc8ad57daa5de6ad8a2', 'name': 'invoices_list_action', 'send_domain': True, 'intent': '', 'active_loop': '', 'condition': '[]', 'action_type': 'KauzaApiCallAction', 'curl_template': "curl -H 'Content-Type: application/json' -H 'Authorization: Bearer {{access_token_slot}}' -X GET 'https://api-kauzapay.onrender.com/factures/me'", 'response': 'None', 'responses': '[{\'template\': \'utter_invoices_list\', \'json_message\': \'{"interactive": {"type": "list", "body": {"text": "Voici une liste des factures que vous avez créer. Cliquez sur l’un pour avoir les détails :"}, "action": {"button": "Factures", "sections": [{"title": "Factures", "rows": [{% for invoice in response %}{"id": "/invoice_detail{{ \\\'{{\\\\"invoice_id\\\\":\\\\"\\\' + invoice[\\\'id\\\'] + \\\'\\\\"}}\\\' }}","title": "{{ invoice[\\\'email\\\'] }}"}{% if not loop.last %},{% endif %}{% endfor %}] }]}}}\'}]', 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "invoices_list_action"




class invoice_detail(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': None, 'name': 'invoice_detail', 'send_domain': True, 'intent': 'invoice_detail', 'active_loop': '', 'condition': [], 'action_type': 'KauzaApiCallAction', 'curl_template': "curl -H 'Content-Type: application/json' -X GET 'https://api-kauzapay.onrender.com'", 'response': None, 'responses': [{'template': 'utter_invoice_detail', 'text': 'Les détails de la facture sont :\\n - Montant: {invoice_amount}\\n - Nom du client: {client_name}\\n - Email du client: {client_email}\\n - Adresse de la boutique : {client_address}\\n - Numéro de téléphone du client: {client_phone_number}\\n - Description: {invoice_description}\\n - Boutique: {invoice_store}'}], 'events': [], 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "invoice_detail"


class balance_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a11efaad57daa5de6ad8a6', 'name': 'balance_action', 'send_domain': True, 'intent': '', 'active_loop': '', 'condition': '[]', 'action_type': 'KauzaApiCallAction', 'curl_template': "curl -H 'Content-Type: application/json' -H 'Authorization: Bearer {{access_token_slot}}' -X GET 'https://api-kauzapay.onrender.com/users/me'", 'response': 'None', 'responses': "[{'template': 'utter_balance', 'text': 'Votre solde actuel est de : {{ solde }} FCFA.'}]", 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "balance_action"



class top_up_account_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a11ffbad57daa5de6ad8a7', 'name': 'top_up_account_action', 'send_domain': True, 'intent': 'string', 'active_loop': 'string', 'condition': '[{}]', 'action_type': 'KauzaApiCallAction', 'curl_template': 'curl -H \'Content-Type: application/json\' -H \'Authorization: Bearer {{access_token_slot}}\' -X POST -d \'{"phone_number": "{{client_phone_number_slot}}", "amount": "{{invoice_amount_slot}}", "network": "TMONEY"}\' \'https://api-kauzapay.onrender.com/recharger\'', 'response': '{}', 'responses': "[{'template': 'utter_top_up_account', 'text': 'Vérifier vos messages et valider le dépot. Votre compte KauzaPay sera alors recharger.'}]", 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "top_up_account_action"




class cash_withdrawal_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a12034ad57daa5de6ad8a8', 'name': 'cash_withdrawal_action', 'send_domain': True, 'intent': 'string', 'active_loop': 'string', 'condition': '[{}]', 'action_type': 'KauzaApiCallAction', 'curl_template': 'curl -H \'Content-Type: application/json\' -H \'Authorization: Bearer {{access_token_slot}}\' -X POST -d \'{"telephone": "{{client_phone_number_slot}}", "montant": "{{invoice_amount_slot}}", "status": "en attente", "reseau": "tmoney"}\'\'https://api-kauzapay.onrender.com\'', 'response': '{}', 'responses': '[{\'template\': \'utter_cash_withdrawal\', \'text\': "Le message de retrait a bien été envoyé à l\'administrateur. Vous recevrez la somme demandé ({{invoice_amount_slot}}) sur le numero suivant : {{client_phone_number_slot}}"}]', 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "cash_withdrawal_action"





class invoice_detail_action(KauzaApiCallAction):
    def __init__(self):
        super().__init__()
        self.agent_config_action = {'id': '68a11dbcad57daa5de6ad8a4', 'name': 'invoice_detail_action', 'send_domain': True, 'intent': '', 'active_loop': '', 'condition': '[]', 'action_type': 'KauzaApiCallAction', 'curl_template': "curl -H 'Content-Type: application/json' -H 'Authorization: Bearer {{access_token_slot}}' -X GET 'https://api-kauzapay.onrender.com/factures/{{invoice_id_slot}}'", 'response': 'None', 'responses': "[{'template': 'utter_invoice_detail', 'text': 'Les détails de la facture sont :\\\\n - Montant: {{amount}}\\\\n - Reference: {{tx_reference}}\\\\n - Email du débiteur: {{email}}\\\\n - Numéro de téléphone du débiteur: {{phone_number}}\\\\n - Description: {{description}}\\\\n - status: {{status}}'}]", 'events': '[]', 'query_slot': 'string', 'created_by': 'auth0|67e4a833d6518eacc30c9a32', 'updated_by': 'auth0|67e4a833d6518eacc30c9a32', 'tenant_id': 'org_PVN2eMvQZWGhqkDx', 'config_id': '689070ffd6907d53dadfea57'}

    def name(self) -> Text:
        return "invoice_detail_action"


