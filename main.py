import json

class DetectiveAIMemory:
    """
    Simulates Cognee's 'unforgettable AI memory' by storing and linking
    disparate pieces of information related to a crime investigation.
    """
    def __init__(self):
        self.facts = [] # Stores all known facts as dictionaries

    def add_fact(self, fact_type, details):
        """
        Adds a new fact to the memory.
        :param fact_type: A string describing the type of fact (e.g., "person", "event", "object").
        :param details: A dictionary containing the specific attributes and relationships of the fact.
                        Values can be strings, numbers, or lists of related entities.
        """
        fact_id = len(self.facts)
        fact_entry = {"id": fact_id, "type": fact_type, **details}
        self.facts.append(fact_entry)
        print(f"Fact {fact_id} added: Type='{fact_type}', Details={details}")

    def query_related_facts(self, entity_name):
        """
        Queries the memory to find all facts that are directly or indirectly
        related to a given entity (person, location, object, etc.).
        This simulates the AI's ability to "remember" and connect information.
        """
        print(f"\n--- Querying connections for '{entity_name}' ---")
        related = []
        entity_name_lower = entity_name.lower()
        for fact in self.facts:
            # Check if the entity_name is present in any value of the fact's details
            # This covers direct mentions in attributes or lists of involved entities.
            for key, value in fact.items():
                if isinstance(value, str) and entity_name_lower in value.lower():
                    related.append(fact)
                    break # Found a match in this fact, move to the next fact
                elif isinstance(value, list) and any(entity_name_lower in str(item).lower() for item in value):
                    related.append(fact)
                    break
        return related

    def print_all_facts(self):
        """Prints all facts currently stored in the memory."""
        print("\n--- All Stored Facts in DetectiveAI Memory ---")
        if not self.facts:
            print("Memory is empty.")
            return
        for fact in self.facts:
            print(json.dumps(fact, indent=2, ensure_ascii=False))
        print("--------------------------------------------")


# --- Main execution --- 
if __name__ == "__main__":
    ai_memory = DetectiveAIMemory()

    # --- Step 1: Ingest various pieces of evidence and information ---
    # This simulates the continuous feeding of data into Cognee's memory,
    # making it 'unforgettable' and ready for connections.

    # Person facts
    ai_memory.add_fact("person", {"name": "Alice Smith", "role": "victim", "status": "deceased"})
    ai_memory.add_fact("person", {"name": "Bob Johnson", "role": "suspect", "known_for": ["violent tendencies", "frequenting local park"]})
    ai_memory.add_fact("person", {"name": "Carol White", "role": "witness", "contact_info": "carol.w@example.com"})

    # Event facts
    ai_memory.add_fact("event", {"type": "stabbing_incident", "location": "Central Park", "time": "2023-10-26 22:00", "involved": ["Alice Smith", "unknown assailant"]})
    ai_memory.add_fact("event", {"type": "discovery_of_body", "location": "Central Park", "time": "2023-10-27 07:30", "reported_by": "Jogger"})

    # Object facts
    ai_memory.add_fact("object", {"name": "Bloody Knife", "type": "weapon", "found_at": "Central Park", "status": "evidence", "fingerprints": ["partial_match_Bob_Johnson"]})
    ai_memory.add_fact("object", {"name": "Alice's Phone", "type": "personal_item", "found_at": "Alice's apartment", "status": "evidence", "last_activity": "2023-10-26 21:45"})

    # Witness statement facts
    ai_memory.add_fact("witness_statement", {"witness": "Carol White", "statement": "Saw Bob Johnson near Central Park around 21:50 on 2023-10-26. He seemed agitated.", "related_to_event": "stabbing_incident"})

    # Forensic report facts
    ai_memory.add_fact("forensic_report", {"report_id": "FR-2023-001", "subject": "Bloody Knife", "findings": "DNA match to Alice Smith, partial fingerprint match to Bob Johnson."})

    # --- Step 2: Query the AI memory to find connections ---
    # This demonstrates how DetectiveAI leverages Cognee's memory to connect dots
    # and reveal insights that might be missed by human investigators.

    # Query for connections related to the victim
    print("\n--- Investigating connections for 'Alice Smith' ---")
    alice_connections = ai_memory.query_related_facts("Alice Smith")
    for fact in alice_connections:
        print(f"  - Fact {fact['id']} ({fact['type']}): {fact}")

    # Query for connections related to the suspect
    print("\n--- Investigating connections for 'Bob Johnson' ---")
    bob_connections = ai_memory.query_related_facts("Bob Johnson")
    for fact in bob_connections:
        print(f"  - Fact {fact['id']} ({fact['type']}): {fact}")

    # Query for connections related to the crime scene
    print("\n--- Investigating connections for 'Central Park' ---")
    park_connections = ai_memory.query_related_facts("Central Park")
    for fact in park_connections:
        print(f"  - Fact {fact['id']} ({fact['type']}): {fact}")

    # Show all stored facts for completeness
    ai_memory.print_all_facts()
