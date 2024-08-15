import pytest
from ChatGPTScraper import ChatGpt


@pytest.fixture(scope="class")
def chatbot():
    """Fixture to initialize ChatGpt and open the chat session."""
    bot = ChatGpt()
    return bot


@pytest.mark.usefixtures("chatbot")
class TestLongMemory:
    def test_arithmetic_chain(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("What is 2 + 2")
        assert responseString == "4"

        responseString = chatbot.sendConversationMessage("square it", 5)
        assert responseString == "16"

        responseString = chatbot.sendConversationMessage("divide it by 2", 7)
        assert responseString == "8"

        responseString = chatbot.sendConversationMessage("find the square root of that value", 9)
        assert responseString == "2√2"

        responseString = chatbot.sendConversationMessage("multiply that by one billion", 11)
        assert responseString == "2000000000√2"
        chatbot.stopScraper()

    def test_conversation(self, chatbot):
        chatbot.openChatGpt()
        responseString = chatbot.sendFirstMessage("Hi, My name is Joe")
        assert "Hello" in responseString, "The response should include a greeting."

        responseString = chatbot.sendConversationMessage("What is your name?", 5)
        assert "Chat" or "ChatGPT" in responseString, "The response should include ChatGPT."

        responseString = chatbot.sendConversationMessage("That's nice, what is your favorite song?", 7)
        assert "music" in responseString, "The response should include a type of music."

        responseString = chatbot.sendConversationMessage("Awesome, do you know where I can find the nearest pharmacy?",
                                                         9)
        assert "go" or "pharmacy" in responseString, "The response should include a location."

        responseString = chatbot.sendConversationMessage("Cool, see you later!", 11)

        assert "goodbye" or "later" in responseString, "The response should include a goodbye."

        chatbot.stopScraper()

