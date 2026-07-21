from elevenlabs.client import ElevenLabs
from keys import elevenlabs_api_key, agent_id, phone_number_id

client = ElevenLabs(
    api_key=elevenlabs_api_key
)
#8200054923
patient = {
    "phone_number": "+919399753907",
    "patient_name": "Ashini",
    "appointment_date": "July 21, 2026",
    "appointment_time": "2:30 PM",
    "provider_name": "Dr. Patel",
    "clinic_name": "Riverside Family Clinic",
    "clinic_address": "123 Main Street, Suite 200",
    "clinic_phone": "+15559876543",
    "appointment_type": "Annual Checkup",
}


response = client.conversational_ai.twilio.outbound_call(
    agent_id=agent_id,
    agent_phone_number_id=phone_number_id,
    to_number=patient["phone_number"],
    conversation_initiation_client_data={
        "dynamic_variables": {
            "patient_name": patient["patient_name"],
            "appointment_date": patient["appointment_date"],
            "appointment_time": patient["appointment_time"],
            "provider_name": patient["provider_name"],
            "clinic_name": patient["clinic_name"],
            "clinic_address": patient["clinic_address"],
            "clinic_phone": patient["clinic_phone"],
            "appointment_type": patient["appointment_type"],
        }
    },
)
print(response)