line_counter = 0
data_header = []
employee = []
customer_USA_list = []
customer = None

with open('customers.csv') as customer_data:

    while True:
        data = customer_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(',')
        else:
            customer = data.split(',')
            if customer[10].upper() == 'USA':
                customer_USA_list.append(customer)
        line_counter += 1

print("Header: \t", data_header)  # 데이터 필드 값 출력

for i in range(0, 10):  # sample 10개만 출력
    # print("Data", i, ":\t\t", customer_list[i])
    print("Data", i, ":\t\t", customer_USA_list[i])
# print(len(customer_list))
print(len(customer_USA_list))

with open('customers_USA_list.csv', 'w') as customer_USA_csv:
    for customer in customer_USA_list:
        customer_USA_csv.write(",".join(customer).strip('\n') + '\n')
