# The UT Findings

---

## Module 1

1. If the `docker run hello-world` does not work, without sudo. 
    - Solution
        1. First, check if the Docker group exists:
            
            ```bash
            getent group docker
            
            ```
            
        2. If the Docker group doesn't exist (unlikely since Docker typically creates it during installation), create it:
            
            ```bash
            sudo groupadd docker
            
            ```
            
        3. Add your user to the Docker group:
            
            ```bash
            sudo usermod -aG docker $USER
            
            ```
            
        4. Apply the new group membership by either:
            - Logging out and back in, or
            - Running this command to apply changes to your current session:
                
                ```bash
                newgrp docker
                
                ```
                
        5. Verify that you can run Docker without sudo:
            
            ```bash
            docker run hello-world
            
            ```
            
        
        If you're still having permission issues, you might need to:
        
        - Check Docker service status: `sudo systemctl status docker`
        - Restart Docker: `sudo systemctl restart docker`
        - In some cases, a system reboot might be needed
        
        This solution adds your user to the Docker group, which gives you permission to use the Docker socket without needing sudo privileges. Keep in mind that this effectively grants your user root-equivalent permissions for Docker operations, so ensure you understand the security implications.
        
2. The Docker installation does not work. The rest of the Packages can be installed but not docker. So as Mentioned in the Documentation Visit the Official Docker Website and Follow the Instructions . 
    - Solution
        1. Uninstall all the docker packages to avoid the Conflict. The instruction is given at the official Docker Website. 
        
        ```bash
        for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
        ```
        
        1. Setup the Docker’s apt repository and Install Docker through apt or its Desktop application.
        
        ```bash
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        ```
        
        1. Verify that the installation is successful by running the `hello-world` image:
            
            ```bash
            sudo docker hello-world
            ```
            

---

## Module 2

1. Not able to reflect any changes from the QML file to Emulator or Device. 
- Solution
    
    Manually Press ctrl + s or Turn on Auto Save in VS Code
    

---

1. Not able to Change the Foreground Color in the PageHeader
    - Solution
        1. Use 
        
        ```json
        StyleHints {        foregroundColor: "orange"    }
        ```
        

---

1. Issue  with the ListView delegate 
- Solution
    1. The height you set for the ListItem is quite small at 3 grid units.
    2. In Ubuntu Touch/Lomiri, ListItem has specific styling and expects certain properties. The Text component might not be appearing because ListItem has its own layout system.
    
    ```json
    ListView {
        id: shoppinglistView
        anchors {
            top: textFieldInput.bottom
            bottom: parent.bottom
            left: parent.left
            right: parent.right
            topMargin: units.gu(2)
        }
        model: shoppinglistModel
        delegate: ListItem {
            // Remove fixed height to let it size naturally
            ListItemLayout {
                title.text: name  // This is the proper way to display text in a ListItem
                title.color: "white"  // Make text visible against the dark background
            }
        }
    }
    ```
    

---

---
