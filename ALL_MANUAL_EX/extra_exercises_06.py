def biggest(num1, num2):
    if num1 > num2:
        return num1
    return num2

def longest_word(word1, word2):
    if len(word1) > len(word2):
        return len(word1)
    return len(word2)

def unsubscribe(my_dict):
    # from datetime import date
    my_dict["subscribed"] = False
    # my_dict["expiry"] = str(date.today())
    # OR, localized:
    import time
    my_dict["expiry"]  = time.strftime("%d/%m/%Y")

# def average_house_price(prices):
#     return f"{sum(prices)/len(prices):.2f}"
# OR, using *args
def average_house_price(*prices):
    return f"{sum(prices)/len(prices):.2f}"


