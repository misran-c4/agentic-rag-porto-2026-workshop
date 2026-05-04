from typing import Any, Dict, List

class SearchTools:
    """
    Provides search and file retrieval utilities over an indexed data store.
    """
    def __init__(self, index, highlighter, file_index: Dict[str, str]):
        self.index = index
        self.highlighter = highlighter
        self.file_index = file_index

    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search the index and return highlighted snippets.

        Args:
            query (str): The search query to look up in the index.

        Returns:
            List of search results with highlighted snippets.
        """
        search_results = self.index.search(query=query, num_results=5)
        return self.highlighter.highlight(query, search_results)

    def get_file(self, filename: str) -> str:
        """
        Retrieve a file's full contents by filename.

        Args:
            filename (str): The filename of the file to retrieve.

        Returns:
            The full file contents, or an error message if not found.
        """
        if filename in self.file_index:
            return self.file_index[filename]
        return f"file {filename} does not exist"