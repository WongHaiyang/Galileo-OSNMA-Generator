# Galileo-OSNMA-Generator
This project implements a forgery scheme for navigation messages containing OSNMA data, and provides the necessary scripts to support  researchers in navigation data forgery, tag generation, OSNMA data filling and other operations. This example is based on test vectors provided by ESA, and all the following operations are explained based on navigation message data from the E02 satellite.

### Navigation Data Forgery

Modify the ionospheric parameter data in the navigation message in the satellite, i.e., change the Ionospheric disturbance flag, and reconstruct the navigation message.
Original data and modified data are reported below for the page 13 in the subframe with WN = 1251, TOW = 277200:

+ 0x054BC11429A07F9FC009C6875D2A80AAAAB21D69F9A18E29635CF8EC0100 (modified)

+ 0x054BC11429A17F9FC009C6875D2A80AAAAB21D69F9A18E29635CF8EC0100 (original)

### Tag Generation

Since tag is associated with the navigation data of the previous subframe, modifying the ionospheric parameter data in the subframe with TOW = 277200 directly results in the failure of the authentication of the first tag in the subframe with TOW = 277230. 
Therefore, the first tag needs to be recalculated and filled to the corresponding field, and the data of each field is first retrieved.
The navigation data retrieved in the subframe with tow=277200 is as follows:

+ 0x1311f898ee1868001f06e7aa04d76d1333662a4249dd4a6ebb4cae193d2a133ff06889eb3f5f823b87f37f405ac4c0bffbfffb11f8001d4e9a00099012f0450a685fe7f000(552 bits, 549 bits without padding)

Retrieve information such as GSTSF=0x4e343aee, PRNA=0x02 from the Mack field. In addition, the field PRND is not required to generate the first tag. The message m used for verification is obtained by connecting different fields above, and the report is as follows:

+ m=0x024e343aee0144c47e263b861a0007c1b9ea8135db44ccd98a909277529baed32b864f4a84cffc1a227acfd7e08ee1fcdfd016b1302ffefffec47e000753a680026404bc11429a17f9fc00 (600 bits)

Retrieve the key from the Mack field in subframe TOW = 277260 as follow:

+ key=0xaca75fbc1c6e40a397ca7ee7ee908870 (128 bits)

Applying the MAC function indicated by the MF field, HMAC-SHA-256. The result of the MAC function is:

+ 0x3c2585c882811fd8b740a5c04ce82c1fc8ca4f722a018a5b32c031f9025f749c (256 bits)

This result is finally truncated to the tag length indicated by the TS field, 40 bits, which is as follows:

+ 0x3c2585c882 (40bit)

### OSNMA Filling

The generated tag is the first tag in this subframe (Tow=277230). Specifically, the 40-bit tag data needs to be filled into the 32-bit Mack field of the first page and the first 8 bits of the Mack field of the second page. 

+ 0x3c2585c8 (32 bits)
+ 0x82 (8 bits)

### CRC Calculation and Filling

Since each page's data requires CRC verification, the CRC value for the modified page data needs to be recalculated and filled into the corresponding field. Below is the reported data of the first page in the subframe with TOW = 2772300, after tag filling and CRC calculation and filling:

+ 0x021333662A4249DD4A6EBB4CAE1900BD2A5C9E8497BA6AAAAA6A9778C100 (240 bits)





