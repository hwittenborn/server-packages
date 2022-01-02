local buildAndPublish() = {
    name: "build-and-publish",
    kind: "pipeline",
    type: "docker",
    steps: [{
        name: "build-and-publish",
        image: "proget.hunterwittenborn.com/docker/makedeb/makedeb:ubuntu-focal",
        environment: {proget_api_key: {from_secret: "proget_api_key"}},
        commands: [
	    "sudo apt-get update",
	    "sudo -E apt-get install python3-requests python3 -y",
            "cd packages/",
            "for i in *; do ../.drone/scripts/publish.py \"$${i}\"; done"
        ]
    }]
};

[
    buildAndPublish()
]
