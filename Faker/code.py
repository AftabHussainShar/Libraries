# ==========================================
# PYTHON FAKER LIBRARY - COMPLETE BASIC GUIDE
# ==========================================

# Install Faker Library
# pip install faker

# Import Faker
from faker import Faker

# Create Faker Object
fake = Faker()

# ==========================================
# 1. BASIC USER INFORMATION
# ==========================================

print("===== BASIC USER INFO =====")

# Random Full Name
print("Name:", fake.name())

# First Name
print("First Name:", fake.first_name())

# Last Name
print("Last Name:", fake.last_name())

# Male Name
print("Male Name:", fake.name_male())

# Female Name
print("Female Name:", fake.name_female())

# Username
print("Username:", fake.user_name())

# Password
print("Password:", fake.password())

print("\n")


# ==========================================
# 2. EMAIL & INTERNET DATA
# ==========================================

print("===== EMAIL & INTERNET =====")

# Email Address
print("Email:", fake.email())

# Company Email
print("Company Email:", fake.company_email())

# Free Email
print("Free Email:", fake.free_email())

# URL / Website
print("Website:", fake.url())

# Domain Name
print("Domain:", fake.domain_name())

# IPv4 Address
print("IPv4:", fake.ipv4())

print("\n")


# ==========================================
# 3. PHONE & ADDRESS
# ==========================================

print("===== PHONE & ADDRESS =====")

# Phone Number
print("Phone:", fake.phone_number())

# Full Address
print("Address:", fake.address())

# City
print("City:", fake.city())

# Country
print("Country:", fake.country())

# Postal Code
print("Postal Code:", fake.postcode())

# Latitude & Longitude
print("Latitude:", fake.latitude())
print("Longitude:", fake.longitude())

print("\n")


# ==========================================
# 4. COMPANY INFORMATION
# ==========================================

print("===== COMPANY DATA =====")

# Company Name
print("Company:", fake.company())

# Company Slogan
print("Catch Phrase:", fake.catch_phrase())

# Business Sentence
print("BS:", fake.bs())

# Job Title
print("Job:", fake.job())

print("\n")


# ==========================================
# 5. DATE & TIME
# ==========================================

print("===== DATE & TIME =====")

# Current Fake Date
print("Date:", fake.date())

# Date Time
print("Date Time:", fake.date_time())

# Year
print("Year:", fake.year())

# Month
print("Month:", fake.month())

# Time
print("Time:", fake.time())

# Future Date
print("Future Date:", fake.future_date())

print("\n")


# ==========================================
# 6. RANDOM NUMBERS & TEXT
# ==========================================

print("===== RANDOM DATA =====")

# Random Integer
print("Random Number:", fake.random_int(min=1, max=100))

# Random Digit
print("Random Digit:", fake.random_digit())

# Random Text
print("Text:", fake.text())

# Random Sentence
print("Sentence:", fake.sentence())

# Random Paragraph
print("Paragraph:", fake.paragraph())

print("\n")


# ==========================================
# 7. FINANCE & INVOICE DATA
# ==========================================

print("===== FINANCE DATA =====")

# Currency Code
print("Currency:", fake.currency_code())

# Credit Card Number
print("Card Number:", fake.credit_card_number())

# Credit Card Provider
print("Card Provider:", fake.credit_card_provider())

# IBAN
print("IBAN:", fake.iban())

# Invoice UUID
print("Invoice ID:", fake.uuid4())

print("\n")


# ==========================================
# 8. PROFILE DATA
# ==========================================

print("===== PROFILE =====")

# Full Profile
profile = fake.profile()

print(profile)

print("\n")


# ==========================================
# 9. GENERATE MULTIPLE USERS
# ==========================================

print("===== MULTIPLE USERS =====")

for i in range(5):
    print({
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city()
    })

print("\n")


# ==========================================
# 10. PAKISTANI DATA
# ==========================================

print("===== PAKISTANI DATA =====")

# Pakistani Locale
pk_fake = Faker('en_PK')

print("Pakistani Name:", pk_fake.name())
print("Pakistani Address:", pk_fake.address())
print("Pakistani Phone:", pk_fake.phone_number())

print("\n")


# ==========================================
# 11. GENERATE DUMMY DATABASE RECORDS
# ==========================================

print("===== DUMMY USERS =====")

users = []

for i in range(3):
    user = {
        "id": i + 1,
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "company": fake.company(),
        "address": fake.address()
    }

    users.append(user)

print(users)

print("\n")


# ==========================================
# END
# ==========================================

print("Fake Data Generation Completed Successfully!")
