import requests
import sys
import pandas as pd

print("#"*90)
print("     Author: Tal Sperling")
print("     Version: 2.0.0")
print("     This code is to be used for educational purposes or legal penetration testing only")
print("     I do not take responsibility for any misuse or illegal action/use of this code")
print("#"*90+"\n")



try:
    urls_to_scan = open(sys.argv[1], 'r')
    keyword = sys.argv[2]
    Lines = urls_to_scan.readlines()

    full_headers = []

    for line in Lines:
        URL = f"https://{line.strip()}"

        print(f"[+] Scanning {line.strip()}")
        try:
            response = requests.get(URL)
            all_headers = response.headers

            

            header_value_pairs = [(header, value) for header, value in all_headers.items()]
            for header, value in all_headers.items():
                is_keyword = False
                if keyword in value:
                    is_keyword = True

                headers_dict = {"URL":URL,"Header":header, "Value":value, "Keyword_Found":is_keyword}
                full_headers.append(headers_dict)
                
                
            
    
           
        except Exception as e:
            print("[-] Connection failed")
            print(e)
            headers_dict = {"URL":URL,"Header":"Connection Failed", "Value":e, "Keyword_Found":""}
            full_headers.append(headers_dict)
    
    main_df = pd.DataFrame(full_headers)
    print(main_df)

    try:
        excel_filename = 'headers_data.xlsx'
        main_df.to_excel(excel_filename, index=False)
        print(f"[+] Data saved to {excel_filename}")
    except Exception as e:
        print("[-] Error")
        print(e)

except Exception as e:
    print("[-] Error")
    print(e)
