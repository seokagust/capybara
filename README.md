# capybara

Código para interpretação e classificação de dados farmacocinéticos e toxicológicos do pkCSM.

## Descrição

Este repositório contém scripts em Python para processar e interpretar dados de propriedades farmacocinéticas e toxicológicas gerados pelo pkCSM (predictive computational models for small molecules). O script principal `pkcsmreader.py` lê um arquivo CSV de entrada contendo dados de propriedades moleculares e adiciona classificações interpretáveis baseadas nos valores numéricos ou categóricos.

## Funcionalidades

O script `pkcsmreader.py` classifica as seguintes propriedades:

- **Solubilidade em água** (Water solubility)
- **Permeabilidade Caco-2** (Caco2 permeability)
- **Absorção intestinal humana** (Intestinal absorption)
- **Permeabilidade cutânea** (Skin permeability)
- **Substrato de P-glicoproteína** (P-glycoprotein substrate)
- **Inibidor de P-glicoproteína** (P-glycoprotein inhibitor)
- **Distribuição no volume de distribuição** (VDss)
- **Fração não ligada** (Fraction unbound)
- **Clearance total** (Total clearance)
- **Toxicidade aguda oral em ratos** (Oral Rat Acute Toxicity)
- **Toxicidade crônica oral em ratos** (Oral Rat Chronic Toxicity)
- **Permeabilidade BBB** (BBB permeability)
- **Permeabilidade CNS** (CNS permeability)
- **Substratos e inibidores de CYP** (CYP substrates/inhibitors)
- **Substrato renal OCT2** (Renal OCT2 substrate)
- **Toxicidade AMES** (AMES toxicity)
- **Dose máxima tolerada** (Max. tolerated dose)
- **Inibidor hERG** (hERG inhibitor)
- **Hepatotoxicidade** (Hepatotoxicity)
- **Sensibilização cutânea** (Skin sensitisation)
- **Toxicidade em T. pyriformis** (T.pyriformis toxicity)
- **Toxicidade em minnow** (Minnow toxicity)

Cada propriedade é classificada em categorias como "Alta", "Moderada", "Baixa", "Sim" ou "Não" com base em thresholds científicos estabelecidos.

## Requisitos

- Python 2.7+ ou Python 3.x
- Biblioteca padrão `csv` (incluída no Python)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seokagust/capybara.git
   cd capybara
   ```

2. Certifique-se de que o Python está instalado no seu sistema.

## Uso

1. Execute o script:
   ```bash
   python pkcsmreader.py
   ```

2. Quando solicitado, digite o nome do arquivo de entrada (com extensão .csv):
   ```
   Nome do arquivo de entrada (com extensão .csv): dados_entrada.csv
   ```

3. Digite o nome do arquivo de saída:
   ```
   Nome do arquivo de saída (com extensão .csv): dados_saida.csv
   ```

O script processará o arquivo de entrada e criará um novo arquivo com as classificações adicionadas.

## Formato dos Arquivos

### Arquivo de Entrada
Arquivo CSV onde:
- A coluna 4 (índice 4) contém o nome da propriedade
- A coluna 5 (índice 5) contém o valor da propriedade

Exemplo:
```
Nome,MW,LogP,HBD,Propriedade,Valor
Molecule1,150.2,2.5,1,water solubility,-1.5
Molecule1,150.2,2.5,1,caco2 permeability,1.2
```

### Arquivo de Saída
O mesmo formato do arquivo de entrada, com uma coluna adicional contendo a classificação:

```
Nome,MW,LogP,HBD,Propriedade,Valor , Classificação
Molecule1,150.2,2.5,1,water solubility,-1.5 , Moderate water solubility
Molecule1,150.2,2.5,1,caco2 permeability,1.2 , High Caco2 Permeability
```

## Exemplos

Para testar o script, você pode usar dados de exemplo do pkCSM ou criar um arquivo CSV simples conforme o formato descrito acima.

## Notas

- O script é compatível com Python 2 e 3.
- Valores inválidos ou não numéricos são tratados adequadamente.
- As classificações são baseadas em thresholds padrão da literatura farmacológica.
- Para propriedades não reconhecidas, nenhuma classificação é adicionada.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
