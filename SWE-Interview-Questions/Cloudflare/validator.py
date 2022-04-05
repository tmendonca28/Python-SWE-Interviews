from datetime import datetime

VALIDATOR_INPUT="""id, address, name
1, 192.168.1.100, agm
2, 192.173.2.12, jww
3, 192.28.3.40, xyz
"""
CURRENT_STATE="""id,time,name,address,created_at,deleted_at
1, 8:00, agm, 192.168.1.100, 8:00, 5:00
2, 8:00, jww, 192.173.2.12, 8:00, 5:00
3, 8:00, xyz, 192.28.3.40, 8:00, 11:00
4, 8:00, agmdf, 192.168.13.100, 8:00, 5:00
"""

def get_validator_ips(validator_input):
    validator_ips = []
    rows = validator_input.split("\n")
    # Use string manipulation to get ips
    for i in range(1, len(rows)-1, 1):
        validator_ips.append(rows[i].split(",")[1])
    return validator_ips

def get_current_state_ips(current_state):
    current_state_data = {}
    rows = current_state.split("\n")
    for i in range(1, len(rows)-1, 1):
        current_state_data[rows[i].split(",")[3]] = rows[i].split(",")[5]
    return current_state_data

def merge_state(current_state_data, val_ips):
    aggregated_output = {}
    curr_ips = list(current_state_data.keys())
    for ip in curr_ips:
        if ip in val_ips:
            aggregated_output[ip] = {
                "status": "UPDATE",
                "deleted_at": current_state_data[ip]
            }
        else:
            aggregated_output[ip] = {
                "status": "CREATE",
                "deleted_at": datetime.now().strftime("%H:%M:%S")
            }
    return aggregated_output


if __name__ == "__main__":
    val_ips = get_validator_ips(VALIDATOR_INPUT)
    current_state_data = get_current_state_ips(CURRENT_STATE)
    aggregated_output = merge_state(current_state_data, val_ips)
    print(aggregated_output)