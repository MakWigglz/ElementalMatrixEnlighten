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
                'sources': [],   # Placeholder for sources
                'urls': [],      # Placeholder for URLs
                'image_urls': [] # Placeholder for image URLs
            }
            self.add_branch(branch)

    def update_branch_content(self, branch_name, content, sources, urls, image_urls):
        for branch in self.branches:
            if branch['name'] == branch_name:
                branch['content'] = content
                branch['sources'] = sources
                branch['urls'] = urls
                branch['image_urls'] = image_urls
                break

# Initialize a TenBranches object
ten_branches = TenBranches()

# Update the content for the "Science" branch
ten_branches.update_branch_content(
    branch_name="Science",
    content="Physics, Chemistry, Biology, Quantum Dynamics, Astronomy",
    sources=["Wikipedia", "Britannica"],
    urls=["https://en.wikipedia.org/wiki/Science", "https://www.britannica.com/science"],
    image_urls=["https://example.com/science.jpg", "https://example.com/science2.jpg"]
)
# Update the content for the "Technology" branch
ten_branches.update_branch_content(
    branch_name="Technology",
    content="Aviation, Military Technology, Computer_Science, Internet, Robotics&AI, Farming Tech., Shipping Tech, Manufacturing.",
    sources=["Wikipedia", "TechCrunch"],
    urls=["https://en.wikipedia.org/wiki/Technology", "https://techcrunch.com"],
    image_urls=["https://example.com/technology.jpg", "https://example.com/technology2.jpg"]
)
# Update the content for the "Engineering" branch
ten_branches.update_branch_content(
    branch_name="Engineering",
    content="Mechanical Engineering, Electrical Engineering, Civil Engineering, Chemical Engineering, Material Science.",
    sources=["Wikipedia", "TechWorld", "Scientific American"],
    urls=["https://en.wikipedia.org/wiki/Engineering", "https://www.techworld.com/engineering", "https://www.scientificamerican.com/magazine/article/engineering-history-101/"],
    image_urls=["https://example.com/engineering.jpg", "https://example.com/engineering2.jpg"]
)
# Update the content for the "Mathematics" branch
ten_branches.update_branch_content(
    branch_name="Mathematics",
    content="Algebra, Calculus, Trigonometry, Statistics, Linear Algebra, Differential Equations.",
    sources=["Wikipedia", "Mathematical Association of America"],
    urls=["https://en.wikipedia.org/wiki/Mathematics", "https://www.maa.org/"],
    image_urls=["https://example.com/mathematics.jpg", "https://example.com/mathematics2.jpg"]
)
# Update the content for the "Art" branch
ten_branches.update_branch_content(
    branch_name="Art",
    content="Painting, Sculpture, Photography, Filmmaking, Literature, Theater.",
    sources=["Wikipedia", "National Gallery of Art"],
    urls=["https://en.wikipedia.org/wiki/Art", "https://www.nga.gov/collections/nga-collection-of-art-and-architecture", "https://www.nationalgeographic.com/adventure/article/history-of-art"],
    image_urls=["https://example.com/art.jpg", "https://example.com/art2.jpg"]
)
# Update the content for the "History" branch
ten_branches.update_branch_content(
    branch_name="History",
    content="Ancient History, Modern History, Archaeology, Politics, Economics.",
    sources=["Wikipedia"],
    urls=["https://en.wikipedia.org/wiki/History"],
    image_urls=["https://example.com/history.jpg"]
)
# Update the content for the "Geography" branch
ten_branches.update_branch_content(
    branch_name="Geography",
    content="Earthquakes, Tsunamis, Volcanoes, Rivers, Oceans, Climate, Topography, Countries, Animal Kingdom.",
    sources=["Wikipedia"],
    urls=["https://en.wikipedia.org/wiki/Geography"],
    image_urls=["https://example.com/geography.jpg"]
)
# Update the content for the "Music" branch
ten_branches.update_branch_content(
    branch_name="Music",
    content="Classical Music, Jazz, Rock, Pop, Hip-Hop, Country, Reggae, Blues, Electronic Music.",
    sources=["Wikipedia", "Musical Index", "The New York Times"],
    urls=["https://en.wikipedia.org/wiki/Music", "https://www.musicalindex.com", "https://www.nytimes.com/section/arts/music"],
    image_urls=["https://example.com/music.jpg", "https://example.com/music2.jpg"]
)
# Update the content for the "Literature" branch
ten_branches.update_branch_content(
    branch_name="Literature",
    content="Novels, Short Stories, Poetry, Essays, Biographies, Autobiographies, History, Fiction, Non-Fiction.",
    sources=["Wikipedia"],
    urls=["https://en.wikipedia.org/wiki/Literature"],
    image_urls=["https://example.com/literature.jpg"]
)
# Update the content for the "Sports" branch
ten_branches.update_branch_content(
    branch_name="Sports",
    content="Basketball, Cricket, Football, Soccer, Hockey, Volleyball, Softball, Rugby, Golf.",
    sources=["Wikipedia", "BeInSports", "Sports Illustrated", "ESPN"],
    urls=["https://en.wikipedia.org/wiki/Sports", "https://www.beinsports.com", "https://www.sportsillustrated.com", "https://www.espn.com"],
    image_urls=["https://example.com/sports.jpg", "https://example.com/sports2.jpg"]
)

# Retrieve and print branches
for branch in ten_branches.get_branches():
    print(f"Branch Name: {branch['name']}")
    print(f"Content: {branch['content']}")
    print(f"Sources: {branch['sources']}")
    print(f"URLs: {branch['urls']}")
    print(f"Image URLs: {branch['image_urls']}")
    print("-----")
    