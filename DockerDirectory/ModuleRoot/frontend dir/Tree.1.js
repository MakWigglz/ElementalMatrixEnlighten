window.Tree = class Tree {
    constructor(container) {
        this.container = container;
        this.branches = [];
        this.numBranches = 10;
        this.topics = [
            "Science", "Technology", "Engineering", "Mathematics",
            "Art", "History", "Geography", "Music", "Literature", "Sports"
        ];
        
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.camera.position.z = 15;
        
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.container.appendChild(this.renderer.domElement);

        this.branchMaterial = new THREE.MeshPhongMaterial({ color: 0x8B4513 });
        this.branchRadius = 0.5;
        this.branchHeight = 2;
        this.branchSegments = 10;
        this.branchAngle = Math.PI / 5;
        this.branchSeparation = 0.2;

        this.raycaster = new THREE.Raycaster();
        this.mouse = new THREE.Vector2();

        window.addEventListener('resize', () => this.onWindowResize(), false);
        window.addEventListener('mousemove', (event) => this.onMouseMove(event), false);
        window.addEventListener('click', (event) => this.onMouseClick(event), false);

        this.init();
    }

    init() {
        this.createBranches();
        this.positionBranches();
        this.addLighting();
        this.animate();
    }

    createBranches() {
        for (let i = 0; i < this.numBranches; i++) {
            const branchGeometry = new THREE.CylinderGeometry(
                this.branchRadius, this.branchRadius / 2, this.branchHeight, this.branchSegments
            );
            const branch = new THREE.Mesh(branchGeometry, this.branchMaterial);
            branch.userData = { topic: this.topics[i], originalColor: this.branchMaterial.color.getHex() };
            this.branches.push(branch);
            this.scene.add(branch);

            // Add leaves or decorations to the branch
            this.addLeaves(branch);
        }
    }

    addLeaves(branch) {
        const leafGeometry = new THREE.SphereGeometry(0.2, 8, 8);
        const leafMaterial = new THREE.MeshPhongMaterial({ color: 0x00FF00 });
        
        for (let i = 0; i < 5; i++) {
            const leaf = new THREE.Mesh(leafGeometry, leafMaterial);
            leaf.position.set(
                Math.random() * 0.5 - 0.25,
                Math.random() * this.branchHeight,
                Math.random() * 0.5 - 0.25
            );
            branch.add(leaf);
        }
    }

    positionBranches() {
        const centerY = this.branchHeight / 2;
        for (let i = 0; i < this.branches.length; i++) {
            const angle = (i / this.branches.length) * Math.PI * 2;
            const radius = 5;
            const x = Math.cos(angle) * radius;
            const z = Math.sin(angle) * radius;
            this.branches[i].position.set(x, centerY, z);
            this.branches[i].rotation.z = -angle + Math.PI / 2;
            this.branches[i].rotation.x = this.branchAngle;
        }
    }

    addLighting() {
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        this.scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(0, 10, 0);
        this.scene.add(directionalLight);
    }

    onMouseMove(event) {
        this.mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

        this.raycaster.setFromCamera(this.mouse, this.camera);

        const intersects = this.raycaster.intersectObjects(this.branches);

        this.branches.forEach(branch => {
            branch.material.color.setHex(branch.userData.originalColor);
        });

        if (intersects.length > 0) {
            const intersectedBranch = intersects[0].object;
            intersectedBranch.material.color.setHex(0xFF0000);
        }
    }

    onMouseClick(event) {
        this.raycaster.setFromCamera(this.mouse, this.camera);

        const intersects = this.raycaster.intersectObjects(this.branches);

        if (intersects.length > 0) {
            const selectedBranch = intersects[0].object;
            const topic = selectedBranch.userData.topic;
            alert(`You clicked on the ${topic} branch!`);
            // Here you can add code to navigate to the topic page or show more information
        }
    }

    animate() {
        requestAnimationFrame(() => this.animate());

        // Rotate the entire scene slowly
        this.scene.rotation.y += 0.005;

        this.renderer.render(this.scene, this.camera);
    }

    onWindowResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
}