import json
from datetime import datetime

def convert_wallabag_to_hoarder(wallabag_json_file, output_file="hoarder_output.json"):
    """
    Converts a Wallabag JSON backup file to Hoarder JSON format,
    reports the number of bookmarks converted, and writes the output to a file.

    Args:
        wallabag_json_file (str): Path to the Wallabag JSON file.
        output_file (str, optional): Path to the output Hoarder JSON file.
                                     Defaults to "hoarder_output.json".

    Returns:
        None
    """
    with open(wallabag_json_file, 'r') as f:
        wallabag_data = json.load(f)

    hoarder_bookmarks = []
    bookmark_count = 0
    for entry in wallabag_data:
        hoarder_bookmark = {
            "createdAt": int(datetime.fromisoformat(entry['created_at'].replace('Z', '+00:00')).timestamp()),
            "title": entry['title'],
            "tags": entry['tags'],
            "content": {
                "type": "link",
                "url": entry['url']
            },
            "note": None
        }
        hoarder_bookmarks.append(hoarder_bookmark)
        bookmark_count += 1

    hoarder_data = {"bookmarks": hoarder_bookmarks}
    hoarder_json_output = json.dumps(hoarder_data, indent=None)

    with open(output_file, 'w') as outfile:
        outfile.write(hoarder_json_output)

    print(f"Converted {bookmark_count} bookmarks and wrote output to {output_file}")

if __name__ == "__main__":
    convert_wallabag_to_hoarder('wallabag.json')
