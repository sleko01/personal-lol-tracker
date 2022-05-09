class APIFetcher:
    api_key = 'RGAPI-7b853924-bcf6-4102-b043-ce3cd689b8ae'
    puuid = 'vRcJBT69hPYI4W5NnxWnDsKY-bI0e1Dih7gTAx5KHzGkZtIJXQ9wjxAWMTTTzrIkF-87544a9GCAvA'

    # api_key and puuid are class attributes since they are used everywhere

    @staticmethod
    def get_api_key():
        return APIFetcher.api_key

    @staticmethod
    def get_puuid():
        return APIFetcher.puuid

    @staticmethod
    def set_puuid(new_puuid):
        APIFetcher.puuid = new_puuid
