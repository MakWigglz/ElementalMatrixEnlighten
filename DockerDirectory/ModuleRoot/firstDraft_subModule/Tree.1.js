constructor(container) 
    this.container = container;
    this.branches = [];
    this.numBranches = 10; // Set the number of branches
    this.topics = [
        "Science", "Technology", "Engineering", "Mathematics",
        "Art", "History", "Geography", "Music", "Literature", "Sports"
    ]; // Add your topics here
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.container.appendChild(this.renderer.domElement);

    this.branchMaterial = new THREE.MeshPhongMaterial({ color: 0x555555 });
    this.branchRadius = 0.5;
    this.branchHeight = 2;
    this.branchSegments = 10;
    this.branchAngle = Math.PI / 5; // 36 degrees
    this.branchSeparation = 0.2;

    this.init();

