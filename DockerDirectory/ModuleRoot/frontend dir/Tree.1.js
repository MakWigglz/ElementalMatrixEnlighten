window.Tree = class Tree {
    constructor(container) {
        this.container = container;
        this.branches = [];
        this.numBranches = 10;
        this.branchRadius = 0.4;
        this.branchHeight = 3;
        this.branchSegments = 12;
        this.branchAngle = Math.PI / 4;
        this.topics = [
            "Science", "Technology", "Engineering", "Mathematics",
            "Art", "History", "Geography", "Music", "Literature", "Sports"
        ];
        
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.camera.position.z = 20;
        this.camera.position.y = 10;
        
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.container.appendChild(this.renderer.domElement);

        this.branchMaterial = new THREE.MeshPhongMaterial({ color: 0x8B4513 });
        this.leafMaterial = new THREE.MeshPhongMaterial({ color: 0x2E8B57 });
        this.branchRadius = 0.3;
        this.branchHeight = 2;
        this.branchSegments = 8;
        this.branchAngle = Math.PI / 6;

        this.raycaster = new THREE.Raycaster();
        this.mouse = new THREE.Vector2();

        window.addEventListener('resize', () => this.onWindowResize(), false);
        window.addEventListener('mousemove', (event) => this.onMouseMove(event), false);
        window.addEventListener('click', (event) => this.onMouseClick(event), false);

        this.init();
    }

    init() {
        this.createTree();
        this.addLighting();
        this.animate();
    }

   createTree() {
    const trunkGeometry = new THREE.CylinderGeometry(0.8, 1, 6, 12);
    const trunk = new THREE.Mesh(trunkGeometry, this.branchMaterial);
    trunk.position.y = 3;
    this.scene.add(trunk);

    this.createBranches(trunk, 0, 6);
    }

  createBranches(parentBranch, depth, length) {
    if (depth > 5) return;

    const numBranches = depth === 0 ? this.numBranches : Math.floor(Math.random() * 3) + 2;
    
    for (let i = 0; i < numBranches; i++) {
        const branchRadius = depth === 0 ? this.branchRadius : this.branchRadius / (depth + 1);
        const branchLength = depth === 0 ? length : length * 0.7;
        
        const branchGeometry = new THREE.CylinderGeometry(
            branchRadius,
            branchRadius * 0.8,
            branchLength,
            this.branchSegments
        );
        const branch = new THREE.Mesh(branchGeometry, this.branchMaterial);
        
        branch.position.y = branchLength / 2;
        branch.rotation.x = Math.random() * this.branchAngle;
        branch.rotation.z = (i / numBranches) * Math.PI * 2;

        if (depth === 0) {
            branch.userData = { topic: this.topics[i], originalColor: this.branchMaterial.color.getHex() };
            this.branches.push(branch);
            // Make main branches more prominent
            branch.scale.set(1.5, 1.2, 1.5);
            }

            parentBranch.add(branch);
        
        this.createBranches(branch, depth + 1, branchLength * 0.7);
        this.addFoliage(branch, depth);
        }
    }
    displayTopicInfo(topicData) {
    const infoPanel = document.getElementById('topic-info');
    infoPanel.innerHTML = `
        <h2>${topicData.title}</h2>
        <p>${topicData.content}</p>
        <img src="${topicData.image_url}" alt="${topicData.title}">
        <p>Source: <a href="${topicData.url}" target="_blank">${topicData.source}</a></p>
    `;
    infoPanel.style.display = 'block';
}
    addFoliage(branch, depth) {
        const foliageGeometry = new THREE.ConeGeometry(0.5 / (depth + 1), 1 / (depth + 1), 8);
        const foliage = new THREE.Mesh(foliageGeometry, this.leafMaterial);
        foliage.position.y = 0.5;
        branch.add(foliage);
    }

    addLighting() {
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        this.scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(5, 10, 5);
        this.scene.add(directionalLight);
    }

    onMouseMove(event) {
        this.mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

        this.raycaster.setFromCamera(this.mouse, this.camera);
        const intersects = this.raycaster.intersectObjects(this.branches);

        this.branches.forEach(branch => {
            if (intersects.length > 0 && intersects[0].object === branch) {
                branch.material.color.setHex(0xFFD700); // Highlight color
            } else {
                branch.material.color.setHex(branch.userData.originalColor);
            }
        });
    }

    onMouseClick(event) {
        this.raycaster.setFromCamera(this.mouse, this.camera);
        const intersects = this.raycaster.intersectObjects(this.branches);

        if (intersects.length > 0) {
            const selectedBranch = intersects[0].object;
            const topic = selectedBranch.userData.topic;
            if (topic) {
                this.loadTopicData(topic);
            }
        }
    }

    loadTopicData(topic) {
        // Simulating API call
        console.log(`Loading data for topic: ${topic}`);
        // In a real scenario, you would fetch data from your backend here
        const mockData = {
            title: topic,
            content: `This is sample content for ${topic}.`,
            image_url: 'https://example.com/image.jpg',
            source: 'Sample Source',
            url: 'https://example.com'
        };
        this.displayTopicInfo(mockData);
    }

    displayTopicInfo(topicData) {
        const infoPanel = document.getElementById('topic-info');
        infoPanel.innerHTML = `
            <h2>${topicData.title}</h2>
            <p>${topicData.content}</p>
            <img src="${topicData.image_url}" alt="${topicData.title}">
            <p>Source: <a href="${topicData.url}" target="_blank">${topicData.source}</a></p>
        `;
        infoPanel.style.display = 'block';
    }

    animate() {
        requestAnimationFrame(() => this.animate());

        // Gentle rotation of the entire tree
        this.scene.rotation.y += 0.002;

        this.renderer.render(this.scene, this.camera);
    }

    onWindowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
}