/**
 * Initializes the 3D tree structure and its components.
 * @param {HTMLElement} container - The HTML element that will contain the 3D tree.
 */
class Tree {
    constructor(container) {
        this.container = container;
        this.branches = [];
        this.numBranches = 10; // Set the number of branches
        this.topics = [
            'Sciences', 'Technology', 'philosophy&creation', 'Politics&Current Affairs',
                    'History', 'Literature', 'Geography', 'Standard Model: theory of everything', 'military-industrial complex'
        ]; // Add your topics here

        class Tree {
            constructor(container) {
                this.container = container;
                this.branches = [];
                this.topics = [
                    'Sciences', 'Technology', 'philosophy&creation', 'Politics&Current Affairs',
                    'History', 'Literature', 'Geography', 'Standard Model: theory of everything', 'military-industrial complex'
                ];
                this.branchMaterial = new Tree.MeshPhongMaterial({ color: 0x555555 });
                this.branchRadius = 0.5;
                this.branchHeight = 2;
                this.branchSegments = 10;
                this.branchAngle = Math.PI / 5; // 36 degrees
                this.branchSeparation = 0.2;
            }

            init() {
                this.createBranches();
                this.createGlobes();
                this.render();
            }

            createBranches() {
                const branchGeometry = new THREE.CylinderGeometry(
                    this.branchRadius,
                    this.branchRadius,
                    this.branchHeight,
                    this.branchSegments
                );

                for (let i = 0; i < this.topics.length; i++) {
                    const branchRotation = new Tree.Euler(0, i * this.branchAngle, 0);
                    const branchPosition = new THREE.Vector3(
                        i * this.branchSeparation,
                        0,
                        0
                    );

                    const branch = new THREE.Mesh(
                        branchGeometry,
                        this.branchMaterial
                    );
                    branch.rotation.setFromEuler(branchRotation);
                    branch.position.copy(branchPosition);
                    this.container.add(branch);
                    this.branches.push(branch);
                }
            }

            createGlobes() {
                const globeGeometry = new THREE.SphereGeometry(0.2, 32, 32);
                const globeMaterial = new THREE.MeshPhongMaterial({
                    color: 0xFFFFFF,
                    emissive: 0x0000FF, // Glow color
                    emissiveIntensity: 0.5
                });

                for (let i = 0; i < this.topics.length; i++) {
                    const globePosition = new THREE.Vector3(
                        0,
                        this.branchHeight + 0.2,
                        0
                    );
                    globePosition.copy(this.branches[i].position);

                    const globe = new THREE.Mesh(globeGeometry, globeMaterial);
                    globe.position.copy(globePosition);
                    this.container.add(globe);
                }
            }

            render() {
                const light = new THREE.DirectionalLight(0xFFFFFF, 1);
                light.position.set(1, 1, 1);
                this.container.add(light);

                const camera = new THREE.PerspectiveCamera(75, this.container.clientWidth / this.container.clientHeight, 0.1, 1000);
                camera.position.set(0, 3, 5);
                camera.lookAt(this.container.position);

                const renderer = new THREE.WebGLRenderer();
                renderer.setSize(this.container.clientWidth, this.container.clientHeight);
                renderer.setPixelRatio(window.devicePixelRatio);
                this.container.appendChild(renderer.domElement);

                const scene = new THREE.Scene();
                scene.add(this.container);

                renderer.render(scene, camera);
            }
        }

    }

    init() {
        // Code to create and render the 3D tree
        // ... (existing code to create the tree structure)
        // Create the branches
        for (let i = 0; i < this.numBranches; i++) {
            const branch = new Branch(this); // Assuming you have a Branch class
            branch.create(); // Assuming Branch has a create method
            this.branches.push(branch);
        }

        // Create glowing globes and add topics
        this.branches.forEach((branch, index) => {
            const globe = new Globe(branch); // Assuming you have a Globe class
            globe.setPosition(branch.getTipPosition()); // Set globe position at branch tip
            globe.glow(); // Assuming Globe has a glow method
            globe.addTopic(this.topics[index]); // Add the corresponding topic to the globe
        });

        // Other methods for handling interactions and updates
    }
}
