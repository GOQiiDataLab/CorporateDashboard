from cryptography.fernet import Fernet
import codecs
response = """
{
    "active_24_hours": "67",
    "activity_time": "261.0 hrs",
    "average_steps": "38.3",
    "avg_sleep": "07h 00m",
    "avg_steps_last_week": "42.19",
    "best_performing_clan": "KKs Team",
    "clan_player_count": "{\"Core\":7,\"Design, E commerce & Warehouse Team\":6,\"Devs Team\":6,\"HR, Admin & Accts\":8,\"KKs Team\":12,\"Strategic Partnership & Health Store\":9,\"Tech Team\":30}",
    "consistent_elites": "{\"User_Image\":{\"60\":\"https:\/\/goqii-app.s3.amazonaws.com\/user\/usercon\/rdm61879\/l_94122_1609610132.jpg\",\"38\":\"https:\/\/goqii-app.s3.amazonaws.com\/user\/usercon\/rdm7984\/l_79867_1516640698.jpg\",\"2\":\"https:\/\/goqii-app.s3.amazonaws.com\/user\/usercon\/rdm96549\/l_25242_1540542969.jpg\"},\"Player_Name\":{\"60\":\"Yasser SUHAIL\",\"38\":\"Vishal Gondal\",\"2\":\"Pravin Shelki\"},\"Lifestyle\":{\"60\":\"elite\",\"38\":\"elite\",\"2\":\"elite\"},\"Clan_Name\":{\"60\":\"KKs Team\",\"38\":\"Core\",\"2\":\"Tech Team\"},\"Lifestyle_Change_Date\":{\"60\":1611619200000,\"38\":1617068384000,\"2\":1624530781000}}",
    "distance_walked": "2911 kms",
    "habits": 1191,
    "health_awareness": "{\"Type\":{\"0\":\"fitness\",\"1\":\"nutrition\",\"2\":\"sleep\",\"3\":\"meditation\"},\"UserID\":{\"0\":74,\"1\":66,\"2\":63,\"3\":31},\"ColorCode\":{\"0\":\"#faa200\",\"1\":\"#00FF00\",\"2\":\"#289df9\",\"3\":\"#ff0000\"}}",
    "healthy_percentage": "{\"healthy_perc\": \"95\", \"unhealthy_perc\": \"5\"}",
    "hra": "71",
    "karma": null,
    "lifestyle_players": "{\"Lifestyle\":{\"0\":\"active\",\"1\":\"elite\",\"2\":\"fit\"},\"UserID\":{\"0\":4,\"1\":64,\"2\":10}}",
    "new_elites": "{\"User_Image\":{\"63\":\"https:\/\/goqii-app.s3.amazonaws.com\/user\/usercon\/rdm7623\/l_61488_1612249450.jpg\",\"19\":\"https:\/\/appcdn.goqii.com\/user\/usercon\/rdm93445\/l_22087_1664443439.jpg\",\"5\":\"https:\/\/appcdn.goqii.com\/user\/usercon\/rdm12076\/l_2327_1665998950.jpg\"},\"Player_Name\":{\"63\":\"DIPTI MANJREKAR\",\"19\":\"Prajakta Chougule\",\"5\":\"Sharad Sonawane\"},\"Lifestyle\":{\"63\":\"elite\",\"19\":\"elite\",\"5\":\"elite\"},\"Clan_Name\":{\"63\":\"KKs Team\",\"19\":\"Tech Team\",\"5\":\"Tech Team\"},\"Lifestyle_Change_Date\":{\"63\":1671991429000,\"19\":1671820502000,\"5\":1671526789000}}",
    "player_count": "78",
    "sleep_quality": "{\"sleepObservation\":{\"0\":\"Excellent\",\"1\":\"Fair\",\"2\":\"Good\",\"3\":\"Poor\"},\"user_count\":{\"0\":10,\"1\":22,\"2\":93,\"3\":14}}",
    "steps_distribution": "{\"category\":{\"0\":\"10km to 30km\",\"1\":\"30km to 50km\",\"2\":\"Above 50km\",\"3\":\"Less than 10km\"},\"UserID\":{\"0\":25,\"1\":31,\"2\":12,\"3\":7}}",
    "top_active_players": "{\"User_Image\":{\"47\":\"https:\/\/goqii-app.s3.amazonaws.com\/user\/usercon\/rdm66832\/l_78455_1502297742.jpg\",\"16\":\"https:\/\/goqii-app.s3.amazonaws.com\/user\/usercon\/rdm68209\/l_69358_1562692387.jpg\",\"49\":\"https:\/\/appcdn.goqii.com\/user\/usercon\/rdm95437\/l_32964_1668705590.jpg\"},\"Player_Name\":{\"47\":\"Anand Sawant\",\"16\":\"Vinod Chaudhary\",\"49\":\"Ankit Rathod\"},\"Lifestyle\":{\"47\":\"elite\",\"16\":\"elite\",\"49\":\"elite\"}}",
    "top_activities": "{\"Activity_Name\":{\"0\":\"meditation\",\"1\":\"walk\",\"2\":\"yoga\",\"3\":\"workout\",\"4\":\"weights\"},\"Number_Of_Times_Activity_Done\":{\"0\":118,\"1\":109,\"2\":29,\"3\":22,\"4\":17}}",
    "under_performing_clan": "Devs Team",
    "water_KPI": "2.47",
    "water_card": "699 ltrs",
    "week_over_week": "{\"Week\":{\"0\":38,\"1\":39,\"2\":40,\"3\":41,\"4\":42,\"5\":43,\"6\":44,\"7\":45,\"8\":46,\"9\":47,\"10\":48,\"11\":49,\"12\":50,\"13\":51,\"14\":52},\"Steps\":{\"0\":2376.0,\"1\":2967.0,\"2\":2786.0,\"3\":2951.0,\"4\":3055.0,\"5\":2567.0,\"6\":3202.0,\"7\":3109.0,\"8\":3263.0,\"9\":3371.0,\"10\":3245.0,\"11\":3662.0,\"12\":3178.0,\"13\":3086.0,\"14\":352.0}}"
}
"""
def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    #print(message)
    key = load_key()
    #encoded_message = message.encode()
    encoded_message = str(message).encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    #print(type(encrypted_message))
    return codecs.decode(encrypted_message, 'UTF-8')
    #a =(codecs.decode(encrypted_message, 'UTF-8'))

    #decrypt_message(a)


def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    print(encrypted_message)
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    dec_msg =decrypted_message.decode()
    print(dec_msg)
    return dec_msg

if __name__ == "__main__":
    #encrypt_message("encrypt this message")
    #generate_key()
     # encrypt_message("""
     # {'data':'bhushan'}
     # """)
    encrypt_message(response)
    #decrypt_message('gAAAAABjqrs5aEbOe7TWEUrqWkNm53yHY6z0gQ0o2u_AiOGiWM8BMqiES5cFkjGbUAZQt4uOXPZNvG54xRRmQB_R1lQg1d9hp1ZoYEHOVU2cA3ugDPFoQg0=')
    #decrypt_message('gAAAAABjqo2swqCT2l58v0VednWBXgO35l1csTSd7NBzOMahCxBudeBa-9XCcCQXoHdd7F_hVQNBhjlCRfSLnjnD7bIVObvxoFhfusYIJRAafW_FMCh0ySM=')