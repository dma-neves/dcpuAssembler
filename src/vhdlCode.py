start = """

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ROM256 is
Port(
	adr : in STD_LOGIC_VECTOR(7 downto 0);
	En : in STD_LOGIC;
	DO : out STD_LOGIC_VECTOR(7 downto 0)
);
end ROM256;

architecture Behavioral of ROM256 is

begin

process(adr, En)
begin

	if En = '0' then
		DO <= "00000000";
	else
		
		case adr is
"""

end = """
            when others => DO <= "00000000";
		end case;
		
	end if;

end process;

end Behavioral;
"""