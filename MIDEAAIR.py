from midea_beautiful import connect_to_cloud, appliance_state
from twilio.rest import Client



conf = {
    "sid": "",
    "auth":,""
    "twilio_to": "+14139928529",
    "twilio_from":""
}

client = Client(conf["sid"],conf["auth"])

cloud = connect_to_cloud(
            account="",  # Account e-mail
            password="",  # Account password
            appname="MSmartHome"
        )

appliance = appliance_state( 
    cloud=cloud,  # Account e-mail
    id=0,  # Appliance id obtained from Midea API 
)

while True:
    if appliance.current_humidity >= 45 and not appliance.tank_full:
        appliance.running(True)
        #text message
        tankLevel = appliance.tankLevel
        msg = "Humidity level reached 45 percent, appliance turned on. Current tank level: " + tankLevel
        client.messages.create(to=conf["twilio_to"], from_=conf["twilio_from"], body=msg)
    elif appliance.current_humidity < 32:
        appliance.running(False)
        #text message - turned off
        tankLevel = appliance.tankLevel
        msg = "Humidity level under 32 percent, appliance turned off. Current tank level: " + tankLevel
        client.messages.create(to=conf["twilio_to"], from_=conf["twilio_from"], body=msg)
    elif appliance.current_humidity >= 45 and appliance.tank_full:
        appliance.running(False)
        #text - full tank
        msg = "Humidity level reached, tank is full: EMPTY THE BUCKET"
        client.messages.create(to=conf["twilio_to"], from_=conf["twilio_from"], body=msg)
    elif appliance.tank_full:
        appliance.running(False)
        msg = "Humidity level good for now, tank is full: EMPTY THE BUCKET"
        client.messages.create(to=conf["twilio_to"], from_=conf["twilio_from"], body=msg)

    #print(f"{appliance!r}")