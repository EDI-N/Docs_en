########################################################################################################################
Signing at the EDIN 2.0 platform
########################################################################################################################

.. початок блоку для Signing

.. |del_key| image:: /_constant/signing/del_key.png

.. _sign:

After initializing the signing library, the system will be able to add a file or hardware key (Token). With :underline:`first` signing in the modal window you need to select a file or token (1), enter the password (2) and press **"Browse"** (3) key to sign:

.. image:: /_constant/signing/file1.png
   :align: center

.. hint::
   **Types of electronic signature files:**

   **АЦСК "Україна"** secret key signature files have the extension **.ZS2** and the following values in file names:

   * Director «DS»
   * Accountant «BS»
   * Employee «SS»
   * Signet «S»
   * Encryption «C»
   * Universal key for printing and encryption «U»

   **АЦСК “ПриватБанк”** secret key signature files have the extension **.jks**. Others **АЦСК** secret key signature files mostly have the extension **Key-6.dat**.

.. image:: /_constant/signing/file2.png
   :align: center

The person whicj perform signing will be automatically displayed when the key is successfully added. The user can add several keys - to select the desired signing for the operation, you need to check the box with the left mouse button and click **"Sign"**:

.. image:: /_constant/signing/file3.gif
   :align: center

The signature form opens with the last selected and ready to sign EDS (subject to the validity of the key and the possibility of signing) for all subsequent signatures during this session (before leaving the "EDI NETWORK" platform):

.. image:: /_constant/signing/file7.gif
   :align: center

Additionally, in the signing window you can click **"More details"** to view information about the signatory. You can use the trash can icon (|del_key|) to delete invalid keys.

After authorization, only the password for the selected key must be entered for further signing with the previously added key(s):

.. image:: /_constant/signing/file4.png
   :align: center

.. image:: /_constant/signing/file5.png
   :align: center

.. кінець блоку для Signing


