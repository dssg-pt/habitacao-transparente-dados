# habitacao-transparente-dados

## Processamento dos dados

Os dados disponibilizados são referentes a 14 de fevereiro de 2025. O processamento consistiu na extração dos dados de uma base de dados MongoDB, seguida de uma pipeline de anonimização para garantir a privacidade dos inquiridos.

## Tranformações aplicadas

Para minimizar o risco de identificação individual, foram implementadas as seguintes transformações:

1. **Remoção de Campos de Texto Livre**
- `comentarios`
- `outra-insatisfacao`
- `outra-estrategia-compra`
- `outra-estrategia-arrendamento`

2. **Remoção de Metadados**
- Identificadores únicos
- Campos de metadados do sistema

3. **Agregação de Campos com Elevada Cardinalidade**
- Campo `freguesia` foi removido devido à elevada taxa de valores únicos
- Campo `nacionalidade` foi binarizado em `portuguesa` e `nao-portuguesa`
- Campo `data_nascimento` foi discretizado em intervalos de 5 anos

Estas transformações seguem as boas práticas de anonimização de dados, reduzindo a granularidade de informações que poderiam, em conjunto, permitir a reidentificação dos inquiridos, mantendo simultaneamente a utilidade analítica do conjunto de dados.

## Dicionário de Dados

| **Campo** | **Descrição** |
| --- | --- |
| situacao-habitacional | Campo obrigatório referente à situação habitacional atual. Poderá conter apenas um dos seguintes valores: [arrendo] (”Arrendo a casa/parte da casa onde vivo”), [comprei] (”Comprei a casa onde vivo”), [outrem] (”Vivo alojado por outrem (com familiares, casa cedida/emprestada, por entidade patronal, etc)”) ou [herdei] (”Herdei a casa onde vivo”). |
| distrito | Campo obrigatório  referente ao distrito onde habita (Portugal continental e ilhas). |
| concelho | Campo obrigatório referente ao concelho onde habita (Portugal continental e ilhas). |
| area-util | Campo obrigatório referente à área útil aproximada da habitação em m². Apenas é considerada a superfície interna habitável, excluindo garagens, jardins, pátios e varandas. Poderá conter apenas um dos seguintes valores: [<20], [21-40], [41-60], [61-80], [81-100] , [101-200], [201-400], [>400] ou [NA] (”Não sei/Não quero responder”). |
| tipo-casa | Campo obrigatório referente ao tipo de habitação. Poderá conter um dos seguintes valores: [apartamento] ou [moradia]. |
| tipologia | Campo obrigatório referente à tipologia da habitação. Poderá conter apenas um dos seguintes valores: [T0], [T1], [T2], [T3], [T4+]. |
| ano-nascimento | Campo obrigatório referente ao ano de nascimento. Apenas são permitidos valores entre 1900 e o ano atual. Os valores foram agrupados em intervalos de 5 anos no processamento dos dados. |
| nacionalidade | Campo obrigatório referente à nacionalidade. Poderá conter apenas um dos seguintes valores [portuguesa] e [nao-portuguesa]. |
| rendimento-anual | Campo obrigatório referente ao rendimento líquido anual atual. Poderá conter apenas um dos seguintes valores: [<7001], [7001-12000], [12001-20000], [20001-35000], [35001-50000], [50001-80000], [>80001]. |
| num-pessoas-nao-dependentes | Campo obrigatório referente ao número de pessoas não dependentes a viver na mesma habitação, para além do próprio. Apenas são permitidos valores entre 0 e 20. |
| num-pessoas-dependentes | Campo obrigatório referente ao número de pessoas dependentes a viver na mesma habitação, para além do próprio. Apenas são permitidos valores entre 0 e 20. |
| situacao-profissional | Campo obrigatório referente à situação profissional. Poderá conter um ou vários dos seguintes valores: [empregado-tempo-inteiro], [empregado-tempo-parcial], [contrato-temporario], [independente], [desempregada], [estudante-tempo-integral], [estudante-tempo-parcial], [aposentado], [licenca] ou [outro]. |
| educacao | Campo obrigatório referente ao nível de escolaridade. Poderá conter apenas um dos seguintes valores: [basico] ("Ensino Básico (1º ao 9º ano)”), [secundario] ("Ensino Secundário (10º ao 12º ano)”), [ensino-profissional] ("Ensino Profissional”), [estudo-superior] ("Alguns créditos de Ensino Superior, mas não completado), [licenciatura] ("Licenciatura”), [mestrado] ("Pós-graduação/Mestrado”), [doutoramento] ("Doutoramento”), [NA] ("Não sei/Não quero responder”) ou [outro]. |
| satisfacao | Campo obrigatório referente ao grau de satisfação com a situação habitacional atual. Poderá conter apenas um dos seguintes valores: [muito-satisfeito], [satisfeito], [indiferente], [insatisfeito], [muito-insatisfeito] ou [NA]. |
| percentagem-renda-paga | Campo obrigatório para situação habitacional [arrendo]. Indica a percentagem da renda paga. São permitidos valores entre 0 e 100, em múltiplos de 5. |
| valor-mensal-renda | Campo obrigatório para situação habitacional [arrendo]. Indica a porção individual da renda paga mensalmente. |
| ano-inicio-arrendamento | Campo obrigatório para situação habitacional [arrendo] referente ao ano de início do arrendamento. Apenas são permitidos valores entre 1900 e o ano atual. |
| rendimento-arrendamento | Campo obrigatório para situação habitacional [arrendo] referente ao rendimento líquido anual individual no início do arrendamento. Poderá conter apenas um dos seguintes valores: [<7001], [7001-12000], [12001-20000], [20001-35000], [35001-50000], [50001-80000], [>80000], [NA] (”Não me recordo”). |
| estrategia-arrendamento | Campo obrigatório para situação habitacional [arrendo] referente à estratégia de arrendamento. Poderá conter um ou vários dos seguintes valores: [sem-ajuda] ("Capital próprio, sem necessidade de ajuda no pagamento da renda”), [apoio-familiar-inicio] ("Precisei de apoio financeiro de familiares para caução ou rendas iniciais.”), [apoio-familiar-actualmente] ("Ainda recebo suporte financeiro de familiares para cobrir os custos da renda.”), [apoio-social] ("Tive apoios de subsídios ou apoios sociais.”), [sub-arrendar-parte-habitacao] ("Coloquei uma parte da minha habitação (quartos/escritório/garagem/etc) para sub-arrendar.”) ou [outra]. |
| insatisfacao-motivos | Campo opcional relativo aos motivos de insatisfação com a situação habitacional. Poderá conter um ou vários dos seguintes valores: [vivo-longe] ("Vivo longe do trabalho”), [habitacao-mau-estado] ("A habitação está em mau estado de conservação ou em más condições”), [falta-espaco] (”Tenho falta de espaço”), [pago-demasiado] ("Sinto que estou a pagar demasiado pela habitação”), [dificuldades-financeiras] ("Tenho dificuldade em arcar com as despesas associadas à habitação”), [financeiramente-dependente] ("Estou financeiramente dependente da ajuda de outros"), [vivo-longe-de-transportes] ("Vivo longe de transportes públicos”), [partilho-casa-com-desconhecidos] ("Partilho a casa com pessoas que não conheço muito bem”), [vivo-zona-insegura] ("Vivo numa zona em que não me sinto seguro”) ou [outro]. |
| valor-compra | Campo obrigatório para situação habitacional [comprei]. Indica o valor de compra da habitação, em euros. |
| ano-compra | Campo obrigatório para situação habitacional [comprei] referente ao ano de compra. Apenas são permitidos valores entre 1900 e o ano atual. |
| estado-conservacao | Campo obrigatório para situação habitacional [comprei] referente ao estado do imóvel na altura da compra. Poderá conter apenas um dos seguintes valores: [raiz] ("Construção de raiz"), [execelente] ("Condições excelentes (eg. recém-construído, renovado, sem necessidade de reparos)”), [bom] ("Condições boas (eg. bom estado geral, sem necessidade de reparos significativos, melhorias apenas cosméticas)”), [medio] ("Condições médias (eg. reparos significativos necessários)”) ou [mau] ("Condições más (eg. reformas substanciais necessárias, substituição de canalização ou instalação elétrica)”). |
| estrategia-compra | Campo obrigatório para situação habitacional [comprei] referente à estratégia de compra. Poderá conter um ou vários dos seguintes valores: [emprestimo] (”Tive acesso a um empréstimo bancário.”), [apoio-familiar] ("Contei com o apoio financeiro da minha família para adquirir o imóvel.”), [trabalho-estrangeiro] ("Trabalhei no estrangeiro para poupar dinheiro e viabilizar a compra.”), [investimento] ("Investi em propriedades adquiridas em leilão.”), [sem-ajuda] ("Utilizei os meus próprios recursos sem recorrer a empréstimos/ajudas externas.”), [apoio-social] ("Tive apoios de subsídios ou apoios sociais.”), [conjunto] ("Comprei em conjunto com outra(s) pessoa(s).”), [arrendar-parte-habitacao] ("Coloquei uma parte da minha habitação (quartos/escritório/garagem/etc) para arrendar.”) ou [outra]. |
| rendimento-liquido-anual-individual-na-compra | Campo obrigatório para situação habitacional [comprei] referente ao rendimento líquido anual individual na altura da compra. Poderá conter apenas um dos seguintes valores: [<7001], [7001-12000], [12001-20000], [20001-35000], [35001-50000], [50001-80000], [>80000], [NA] (”Não me recordo”). |
| rendimento-liquido-anual-conjunto-na-compra | Campo obrigatório para situação habitacional [comprei] referente ao rendimento líquido anual conjunto (das pessoas envolvidas na compra da casa) na altura da compra. Poderá conter apenas um dos seguintes valores: [<7001], [7001-12000], [12001-20000], [20001-35000], [35001-50000], [50001-80000], [>80000], [NA] (”Não me recordo”). |
| ano-heranca-aquisicao | Campo obrigatório para situação habitacional [herdei] referente ao ano de aquisição da habitação. Apenas são aceites valores entre 1900 e o ano atual. |
| rendimento-liquido-anual-individual-na-aquisicao | Campo obrigatório para situação habitacional [herdei] referente ao rendimento líquido anual individual na altura da aquisição. Poderá conter apenas um dos seguintes valores: [<7001], [7001-12000], [12001-20000], [20001-35000], [35001-50000], [50001-80000], [>80000], [NA] (”Não me recordo”). |
| rendimento-heranca-conjunto | Campo obrigatório para situação habitacional [herdei] referente ao rendimento líquido anual conjunto (das pessoas envolvidas na aquisição da casa) na altura da aquisição. Poderá conter apenas um dos seguintes valores: [<7001], [7001-12000], [12001-20000], [20001-35000], [35001-50000], [50001-80000], [>80000], [NA] (”Não me recordo”). |
| estado-conservacao-heranca | Campo obrigatório para situação habitacional [herdei] referente ao estado do imóvel na altura da aquisição. Poderá conter apenas um dos seguintes valores: [raiz] ("Construção de raiz"), [execelente] ("Condições excelentes (eg. recém-construído, renovado, sem necessidade de reparos)”), [bom] ("Condições boas (eg. bom estado geral, sem necessidade de reparos significativos, melhorias apenas cosméticas)”), [medio] ("Condições médias (eg. reparos significativos necessários)”) ou [mau] ("Condições más (eg. reformas substanciais necessárias, substituição de canalização ou instalação elétrica)”). |
