phone = {'iphone': 60000, 'redmi': 15000, 'vivo': 30000, 'moto': 19000}

# Print headers
print("Phone Brand      | Price")
print("=================|=======")

# Loop through the dictionary and print in columns
for brand, price in phone.items():
    print(f" {brand:<15} | {price:<10} *")
    
    
