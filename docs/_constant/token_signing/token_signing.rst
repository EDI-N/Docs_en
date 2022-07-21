########################################################################################################################
Signing with Token at EDIN 2.0 platform
########################################################################################################################

.. початок блоку для TokenSign

.. |del_key| image:: /_constant/signing/del_key.png

Full instructions for setting up token signing are available at the following `link <https://wiki.edin.ua/uk/latest/general_2_0/Robota_z_tokenom.html>`__.

.. important::
   Signing is possible only if your token is physically connected to the device (USB port) from which signing will be performed.

The Користувач ЦСК signature web-library (installed on the computer) must be launched:

.. image:: /_constant/token_signing/token_signing_001.png
   :align: center

During the initial initialization of the signature library, confirm the permission of the website to the Користувач ЦСК signature library, click — **"OK"** :

.. image:: /_constant/token_signing/token_signing_002.png
   :align: center

.. image:: /_constant/token_signing/token_signing_003.png
   :align: center

At the :underline:`first` signing in the modal window, you need to **"Select Token"** (1), choose a key (2), enter a password (3), **"Browse"** (4) and **"Add"** (5) active key: 

.. image:: /_constant/token_signing/token_signing_004.png
   :align: center
   :width: 800 px

The user may have several keys added - to select the one required for the signing operation, you need to mark it with the left mouse button and press **"Sign"**:

.. image:: /_constant/token_signing/token_signing_005.png
   :align: center

.. warning::
   If signing with this key has already been done or inconsistency of EDRPOU/TIN data is found (verification), then signing is blocked, and the user is given the appropriate message:

   .. image:: /_constant/token_signing/token_signing_006.png
      :align: center

Additionally, in the signing window you can click **"More details"** to view information about the signatory. You can use the trash can icon (|del_key|) to delete invalid keys.

When working with the previously added key/s, you only need to enter the password for the selected key (steps 2-4 at the figures).

.. кінець блоку для TokenSign


