input1 = input("Enter what mode you would like to use: ")

if input1 == "stock":
    input2 = input("Would you like to analyze or predict: ")
    if input2 == "analyze":
        import stockchart
    if input2 == "predict":
        print("This function is not ready yet")





if input1 == "crypto":
    import crypto