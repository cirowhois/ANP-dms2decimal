# O que é?
A Agência Nacional do Petróleo (ANP) disponibiliza para acesso, consulta e download os dados de Revendedores de Combustível do Brasil. Nos últimos anos este serviço de consulta passou por diversas mudanças e hoje está em [Consulta de Postos](https://cdp.anp.gov.br/ords/r/cdp_apex/consulta-dados-publicos-cdp/consulta-de-postos-lista?).

## Problema
Ao exportar a base completa com tancagem, além das colunas de combustíveis e bicos o sistema disponibiliza as colunas de latitude e longitude do posto.
Isso é excelente, pois muitos postos ficam na beira de estradas e rodovias e isso dificulta um processo de geocodificação automática acurado.
O problema é que estes dados vêm no formato de **Graus, Minutos e Segundos**, necessitando uma conversão para o formato de **Graus Decimais**, uma vez que nem todos os sistemas e/ou banco de dados são preparados para recebê-los assim.
