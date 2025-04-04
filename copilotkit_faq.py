faq_dict = {
    "Can I pass LangGraph message kwargs to CopiloKitChat?": """
    Yes, you absolutely can pass additional metadata through messages from LangGraph to CopilotKit's frontend!

    Use copilotkit_emit_state(config, {"custom_metadata": "value"}) to send intermediate state updates with metadata.

    For more control during long-running operations, you can use copilotkit_emit_message to send customized message content.

    If you specifically need to track which node emitted a message or control frontend display options, you can include that in the state updates.

    Check these docs:
    https://docs.copilotkit.ai/reference/sdk/python/LangGraph#copilotkit_emit_state
    https://docs.copilotkit.ai/coagents/tutorials/agent-native-app/step-8-progressive-state-updates#create-a-copilotkit_customize_config-and-emit-intermediate-state
    """,

    "Hey team, I'm looking for guidance on how to implement \"thinking\" step in chat, similar to what you would see in ChatGPT with reasoning enabled or Cursor chat agent with thinking enabled.": """
    Yes, this is possible and we show this in action in the Research Canvas.

    We call it Predictive State Updates and this docs page goes over how to implement it:
    https://docs.copilotkit.ai/coagents/generative-ui/agentic?language=TypeScript#simulate-state-updates

    If I remember correctly, you are using LangGraph JS, which is included in our documentation examples.

    We have another example for the Travel App tutorial (it's in Python) but take a look at it and let me know if this helps:
    https://docs.copilotkit.ai/coagents/tutorials/ai-travel-app/step-5-stream-progress
    """,

    "LangGraph agent with HITL interrupt works in studio, but behaves strangely with copilotkit": """
    Thank you for flagging this. Would you mind creating a GitHub Issue which will auto-generate a ticket to flag this to the engineering team?
    https://github.com/CopilotKit/CopilotKit/issues
    """,

    "How do I install CopilotKit in my project?": """
    You can install CopilotKit using your package manager of choice. Here's the command for npm:

    npm install @copilotkit/react-ui @copilotkit/react-core
    """,

    "Where do I get the Copilot Cloud Public API Key?": """
    Navigate to Copilot Cloud and follow the instructions to get a public API key. It's free!
    """,

    "How do I setup the CopilotKit provider in my app?": """
    Wrap the <CopilotKit> component around the parts of your app that need to access CopilotKit. For most use-cases, wrap your entire app in layout.tsx:

    import { CopilotKit } from "@copilotkit/react-core";

    <CopilotKit publicApiKey="<your-copilot-cloud-public-api-key>">
        {children}
    </CopilotKit>
    """,

    "How do I setup the Copilot UI?": """
    Import the default styles in your root component (like layout.tsx):

    import "@copilotkit/react-ui/styles.css";

    Then choose and use a built-in UI component such as CopilotPopup, CopilotSidebar, CopilotChat, or Headless UI.
    """,

    "What is CopilotPopup and how do I use it?": """
    CopilotPopup is a floating chat interface that wraps around CopilotChat. It lives at the same level as your main content and can be toggled on/off.

    Example:

    import { CopilotPopup } from "@copilotkit/react-ui";

    <CopilotPopup
        instructions={"You are assisting the user as best as you can. Answer in the best way possible given the data you have."}
        labels={{
            title: "Popup Assistant",
            initial: "Need any help?",
        }}
    />
    """,

    "What is Human-in-the-Loop (HITL)?": """
    Human-in-the-loop (HITL) allows agents to request human input or approval during execution, making AI systems more reliable and trustworthy.

    This pattern is essential for AI applications that involve complex decisions or require human judgment.
    """,

    "When should I use Human-in-the-Loop (HITL)?": """
    HITL is useful when you want to combine the efficiency of AI with human oversight. Use it for:

    - Quality Control: Add human checks at critical decision points
    - Edge Cases: Handle low-confidence or ambiguous situations
    - Expert Input: Get human expertise where needed
    - Reliability: Build a more robust system for real-world usage
    """,

    "How can I implement HITL in CopilotKit using LangGraph?": """
    CopilotKit provides two main approaches to implement HITL with LangGraph:

    1. **Interrupt-based**: Pause the agent using LangGraph's `interrupt` function and wait for user input. This is the recommended starting point.
    2. **Node-based**: Create custom nodes and tools that define HITL behavior within the graph logic.
    """,

    "Where can I learn more about HITL in LangGraph?": """
    You can learn more from LangGraph's concept guide on HITL:
    https://docs.langgraph.dev/concepts/human-in-the-loop
    """,

    "Is there a demo showing HITL in action with CopilotKit?": """
    Yes! The AI Travel App demo video shows an example of HITL in action using CopilotKit to get user feedback mid-execution.
    """
}
