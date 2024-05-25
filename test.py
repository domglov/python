from simple_salesforce import Salesforce

# Salesforce login credentials
USERNAME = 'your_salesforce_username'
PASSWORD = 'your_salesforce_password'
SECURITY_TOKEN = 'your_salesforce_security_token'
DOMAIN = 'login'  # For production use 'login.salesforce.com', for sandbox use 'test'

# Initialize Salesforce client
sf = Salesforce(username=USERNAME, password=PASSWORD, security_token=SECURITY_TOKEN, domain=DOMAIN)

def query_opportunities():
    # Define SOQL query to retrieve Opportunity records
    query = """
        SELECT Id, Name, StageName, CloseDate, Amount
        FROM Opportunity
        LIMIT 10
    """
    
    # Execute query
    result = sf.query_all(query)
    
    # Extract Opportunity records from query result
    opportunities = result['records']
    
    # Print Opportunity details
    for opportunity in opportunities:
        print(f"Opportunity Name: {opportunity['Name']}")
        print(f"Stage: {opportunity['StageName']}")
        print(f"Close Date: {opportunity['CloseDate']}")
        print(f"Amount: {opportunity['Amount']}")
        print("")

if __name__ == "__main__":
    query_opportunities()
