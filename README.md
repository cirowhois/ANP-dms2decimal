## Uso
O `converter_latlong` converte as lat longs de postos de combustível disponbilizadas pela ANP no formato específico ```-22:20:40,647   -49:03:46,018``` para ```-22.344624166667   -49.062782777778```.
Único argumento é o `DataFrame` de entrada.


## Problema
A Agência Nacional do Petróleo (ANP) disponibiliza para acesso, consulta e download os dados de Revendedores de Combustível do Brasil. Nos últimos anos este serviço de consulta passou por diversas mudanças e hoje está em [Consulta de Postos](https://cdp.anp.gov.br/ords/r/cdp_apex/consulta-dados-publicos-cdp/consulta-de-postos-lista?).

<img title="Home Page" alt="Home Page" src="img\homepage.png">

Ao exportar a base completa com tancagem, além das colunas de combustíveis e bicos o sistema disponibiliza as colunas de latitude e longitude do posto.
Isso é excelente, pois muitos postos ficam na beira de estradas e rodovias e isso dificulta um processo de geocodificação automática acurado.
O problema é que estes dados vêm no formato de **Graus, Minutos e Segundos** separados por **:**, necessitando uma conversão para o formato de **Graus Decimais**, uma vez que nem todos os sistemas e/ou bancos de dados são preparados para recebê-los assim.

<img title="Processo" alt="Processo" src="img\process.png">

## Exemplo de uso
Conversão e plotagem dos dados convertidos usando o GeoPandas no arquivo `exemplo.ipynb`.