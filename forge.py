
    # main.py

from llm.ollama_llm import OllamaLLM

from state.project_state import ProjectState

from registry.agent_registry import AgentRegistry

from communication.event_bus import EventBus


from agents.ceo_agent import CEOAgent

from agents.architect_agent import ArchitectAgent

from agents.planner_agent import PlannerAgent

from agents.developer_agent import DeveloperAgent

from agents.frontend_agent import FrontendAgent



# ----------------------

# Setup

# ----------------------

llm = OllamaLLM(

    model="qwen3"

)


state = ProjectState()


registry = AgentRegistry()


event_bus = EventBus(

    registry

)


memory = {}



# ----------------------

# Agents

# ----------------------

ceo = CEOAgent(

    "CEO",

    memory,

    event_bus,

    state,

    llm

)


architect = ArchitectAgent(

    "Architect",

    memory,

    event_bus,

    state,

    llm

)


planner = PlannerAgent(

    "Planner",

    memory,

    event_bus,

    state,

    llm

)


developer = DeveloperAgent(

    "Developer",

    memory,

    event_bus,

    state,

    llm

)


frontend = FrontendAgent(

    "Frontend",

    memory,

    event_bus,

    state,

    llm

)



# ----------------------

# Register agents

# ----------------------

registry.register(

    ceo

)

registry.register(

    architect

)

registry.register(

    planner

)

registry.register(

    developer

)

registry.register(

    frontend

)



# ----------------------

# Product Idea

# ----------------------

state.update(

    "idea",

    "AI Powered Book Recommendation Platform"

)



# ----------------------

# Run Pipeline

# ----------------------

print()

print("="*60)

print("CEO")

print("="*60)

ceo.think()

ceo.act()



print()

print("="*60)

print("ARCHITECT")

print("="*60)

architect.think()

architect.act()



print()

print("="*60)

print("PLANNER")

print("="*60)

planner.think()

planner.act()



print()

print("="*60)

print("DEVELOPER")

print("="*60)

developer.think()

developer.act()



print()

print("="*60)

print("FRONTEND")

print("="*60)

frontend.think()

frontend.act()



# ----------------------

# Messages

# ----------------------

print()

print("="*60)

print("EVENT HISTORY")

print("="*60)


for msg in event_bus.get_history():

    print(msg)



# ----------------------

# State

# ----------------------

print()

print("="*60)

print("PROJECT STATE")

print("="*60)


print()

print("Idea:")

print(

    state.get(

        "idea"

    )

)


print()

print("PRD:")

print(

    state.get(

        "prd"

    )

)


print()

print("Architecture:")

print(

    state.get(

        "architecture"

    )

)


print()

print("Tasks:")

print(

    len(

        state.get(

            "tasks"

        )

    )

)


print()

print("Backend Files:")

print(

    len(

        state.get(

            "backend_files"

        )

    )

)


print()

print("Frontend Files:")

print(

    len(

        state.get(

            "frontend_files"

        )

    )

)