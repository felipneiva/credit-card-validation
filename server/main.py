from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import CreditCard
from datetime import date

app = FastAPI()

def luhn_algorithm(card_number: str):
    total_sum = 0
    parity = len(card_number) % 2

    for i in range(len(card_number)):
        digit = int(card_number[i])

        if (i % 2) == parity:
            digit *= 2
            if digit > 9:
                digit -= 9

        total_sum += digit

    return total_sum % 10 == 0

@app.post("/credit-card")
async def validate_credit_card(credit_card: CreditCard):

    if not credit_card.number.isdigit():
        raise HTTPException(status_code=400, detail="Credit card number must be numeric")
    if not credit_card.cvv.isdigit():
        raise HTTPException(status_code=400, detail="CVV must be numeric")
    if len(credit_card.number) < 16 or len(credit_card.number) > 19:
        raise HTTPException(status_code=400, detail="Credit card number must be between 16 and 19 digits")
    if credit_card.number[:2] in ['34', '37']:
        if len(credit_card.cvv) != 4:
            raise HTTPException(status_code=400, detail="CVV must be exactly 4 digits")
    else:
        if len(credit_card.cvv) != 3:
            raise HTTPException(status_code=400, detail="CVV must be exactly 3 digits")
    if credit_card.expiration_date <= str(date.today()):
        raise HTTPException(status_code=400, detail="Expiration date must be in the future")
    if not luhn_algorithm(credit_card.number):
        raise HTTPException(status_code=400, detail="Invalid credit card number")
    
    return {"status": "ok"}