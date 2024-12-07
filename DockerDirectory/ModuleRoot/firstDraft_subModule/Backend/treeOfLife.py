class TreeOfLife:
    def __init__(self):
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def get_branches(self):
        return self.branches


class TenBranches(TreeOfLife):
    def __init__(self):
        super().__init__()
        self.topics = [
            "Science", "Technology", "Engineering", "Mathematics",
            "Art", "History", "Geography", "Music", "Literature", "Sports"
        ]
        self.initialize_branches()

    def initialize_branches(self):
        for topic in self.topics:
            branch = {
                'name': topic,
                'content': None,  # Placeholder for content
                'source': None,   # Placeholder for source
                'url': None,      # Placeholder for URL
                'image_url': None # Placeholder for image URL
            }
            self.add_branch(branch)

    def update_branch_content(self, branch_name, content, source, url, image_url):
        for branch in self.branches:
            if branch['name'] == branch_name:
                branch['content'] = content
                branch['source'] = source
                branch['url'] = url
                branch['image_url'] = image_url
                break
# Initialize a TenBranches object
ten_branches = TenBranches()        
# retrieve branches  
for branch in ten_branches.get_branches():
    print(f"Branch Name: {branch['name']}")
    print(f"Content: {branch['content']}")
    print(f"Source: {branch['source']}")
    print(f"URL: {branch['url']}")
    print(f"Image URL: {branch['image_url']}")
    print("-----")  
            