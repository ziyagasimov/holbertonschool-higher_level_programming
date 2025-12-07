import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template string and a list of attendee dictionaries.
    """

    # ----------- Type Checking -----------
    if not isinstance(template, str):
        print("Error: Template must be a string. Received:", type(template).__name__)
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # ----------- Empty Input Handling -----------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ----------- Process Each Attendee -----------
    for i, attendee in enumerate(attendees, start=1):

        # Safely get each required value or use "N/A" for missing/None values
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Create a personalized invitation
        output_text = (
            template.replace("{name}", name)
                    .replace("{event_title}", event_title)
                    .replace("{event_date}", event_date)
                    .replace("{event_location}", event_location)
        )

        # Output file name
        filename = f"output_{i}.txt"

        # Write to the output file
        try:
            with open(filename, "w") as f:
                f.write(output_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue

    # Optionally show success message
    print("Invitation files generated successfully.")