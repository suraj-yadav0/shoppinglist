The UT Findings
===============


Module 1
--------

1. If the ``docker run hello-world`` does not work, without sudo.

   -  Solution

      1. First, check if the Docker group exists:

         .. code:: bash

            getent group docker

      2. If the Docker group doesn’t exist (unlikely since Docker
         typically creates it during installation), create it:

         .. code:: bash

            sudo groupadd docker

      3. Add your user to the Docker group:

         .. code:: bash

            sudo usermod -aG docker $USER

      4. Apply the new group membership by either:

         -  Logging out and back in, or

         -  Running this command to apply changes to your current
            session:

            .. code:: bash

               newgrp docker

      5. Verify that you can run Docker without sudo:

         .. code:: bash

            docker run hello-world

      If you’re still having permission issues, you might need to:

      -  Check Docker service status: ``sudo systemctl status docker``
      -  Restart Docker: ``sudo systemctl restart docker``
      -  In some cases, a system reboot might be needed

      This solution adds your user to the Docker group, which gives you
      permission to use the Docker socket without needing sudo
      privileges. Keep in mind that this effectively grants your user
      root-equivalent permissions for Docker operations, so ensure you
      understand the security implications.

  

2. The Docker installation does not work. The rest of the Packages can
   be installed but not docker. So as Mentioned in the Documentation
   Visit the Official Docker Website and Follow the Instructions .

   -  Solution

      1. Uninstall all the docker packages to avoid the Conflict. The
         instruction is given at the official Docker Website.

      .. code:: bash

         for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

      1. Setup the Docker’s apt repository and Install Docker through
         apt or its Desktop application.

      .. code:: bash

         sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

      1. Verify that the installation is successful by running the
         ``hello-world`` image:

         .. code:: bash

            sudo docker hello-world

--------------

Module 2
--------

1. Not able to reflect any changes from the QML file to Emulator or
   Device.

-  Solution

   Manually Press ctrl + s or Turn on Auto Save in VS Code

--------------

1. Not able to Change the Foreground Color in the PageHeader

   -  Solution

      1. Use

      .. code:: json

         StyleHints {        foregroundColor: "orange"    }

--------------

1. Issue with the ListView delegate

-  Solution

   1. The height you set for the ListItem is quite small at 3 grid
      units.
   2. In Ubuntu Touch/Lomiri, ListItem has specific styling and expects
      certain properties. The Text component might not be appearing
      because ListItem has its own layout system.

   .. code:: json

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

--------------

Module 3
--------

1. The Docs Provide some links to UBports API docs. But all these links
   lead to the same place. So it is confusing to find the right link.

--------------

1. The Buttons in the Row are not working. → 3.4 in the Docs

-  Solution 3.4

   The **buttons inside the ``Row`` layout at the bottom** may not be
   functioning as expected due to **conflicts with the ``ListView``
   layout constraints**, **z-index**, or overlapping items.

   Update the ``ListView``\ ’s ``bottom`` anchor to stop before hitting
   the ``Row``:

   .. code:: jsx

      bottom: buttonRemoveAll.top

--------------

Module 4
--------

1. Odd Rows Become Invisible during 5.1 while Creating Property for
   Selection Mode

-  Solution to 5.1

   The root cause of odd-numbered rows appearing *invisible* in your
   ``ListView`` implementation stems from the improper layering of the
   ``Rectangle`` that is intended to alternate the row background color.
   Here’s the Corrected Code

   .. code:: jsx

      delegate: ListItem {
          Rectangle {
              anchors.fill: parent
              z: -1  // explicitly set z-index to ensure it's beneath
              color: index % 2 ? theme.palette.normal.selection : theme.palette.normal.background
          }

          leadingActions: ListItemActions {
              actions: [
                  Action {
                      iconName: "delete"
                      onTriggered: shoppinglistModel.remove(index)
                  }
              ]
          }

          trailingActions: ListItemActions {
              actions: [
                  Action {
                      iconName: "info"
                      onTriggered: console.log(i18n.tr("Info trailing button pressed"))
                  }
              ]
          }

          CheckBox {
              id: itemCheckbox
              visible: root.selectionMode
              anchors {
                  left: parent.left
                  leftMargin: units.gu(2)
                  verticalCenter: parent.verticalCenter
              }
          }

          Text {
              id: itemText
              text : name
              anchors {
                  left: root.selectionMode ? itemCheckbox.right : parent.left
                  leftMargin: root.selectionMode ? units.gu(1) : units.gu(2)
                  verticalCenter: parent.verticalCenter
              }
          }
      }