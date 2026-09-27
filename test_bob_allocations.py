import json
import os

def verify_workspace():
    config_path = "My-Organization/bob_engine_config.json"
    if not os.path.exists(config_path):
        print("❌ Error: Verification matrix blueprint file is missing!")
        return False
        
    with open(config_path, "r") as file:
        data = json.load(file)
        
    balance = data["allocations"]["initial_balance"]
    allocated = data["allocations"]["allocated_spend"]
    
    print(f"🤖 Initializing engine tracking structure for: {data['engine']['name']}")
    print(f"🪙 Verifying Bobcoin Wallet: {balance} BC detected.")
    
    if balance == 40 and allocated == 40:
        print("✅ Success: All 40 Bobcoins verified and bound to current SaaS setup configuration!")
        return True
    else:
        print("❌ Allocation validation fault detected.")
        return False

if __name__ == "__main__":
    verify_workspace()
