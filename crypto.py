
# Import FastMCP for creating the MCP server
from mcp.server.fastmcp import FastMCP
# Import requests for making HTTP requests
import requests


# Initialize the MCP server with the name "Crypto"
mcp = FastMCP("Crypto")

@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Gets the price of a cryptocurrency.
    Args:
        crypto: symbol of the cryptocurrency (e.g., 'bitcoin', 'ethereum').
    """
    try:
        # API endpoint for CoinGecko simple price
        url = f"https://api.coingecko.com/api/v3/simple/price"
        # Prepare parameters for the API call
        params = {"ids": crypto.lower(), "vs_currencies": "usd"}
        # Make the GET request to CoinGecko
        response = requests.get(url, params=params, timeout=10)
        # Raise an error if the request failed
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()
        # Extract the USD price for the given crypto
        price = data.get(crypto.lower(), {}).get("usd")
        if price is not None:
            # Return formatted price if found
            return f"The price of {crypto} is ${price} USD."
        else:
            # Handle case where price is not found
            return f"Price for {crypto} not found."
    except Exception as e:
        # Handle any errors during the request
        return f"Error fetching price for {crypto}: {e}"
    

# Start the MCP server if this script is run directly
if __name__ == "__main__":
    mcp.run()