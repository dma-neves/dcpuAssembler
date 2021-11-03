start = """

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ROM is
Port(
	adr : in STD_LOGIC_VECTOR(15 downto 0);
	En : in STD_LOGIC;
	DO : out STD_LOGIC_VECTOR(15 downto 0)
);
end ROM;

architecture Behavioral of ROM is

begin

process(adr, En)
begin

	if En = '0' then
		DO <= "0000000000000000";
	else
		
		case adr is
"""

end = """
            when others => DO <= "0000000000000000";
		end case;
		
	end if;

end process;

end Behavioral;
"""