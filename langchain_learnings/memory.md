# Memory Types
- ConversationBufferMemory
    - This memory allows for storing of messages and then extracts the messages in a variable

- ConversationBufferWindowMemory
    - Keeps a list of interactions of the conversation over time, it only uses the last K interactions

- ConversationTokenBufferMemory
    - This memory keeps a buffer of recent interactions in mememory and uses token length rather than number of interactions to determine when to flush interactions

- ConversationSummaryMemory
    - This memory creates a summary of the conversation over time

- Vector data memory
    - Stores text in a vector database and retrieves the most relevant blocks of text

- Entity memories
    - Using an LLM, it remembers details about specific entities