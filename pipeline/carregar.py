"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""
import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    
    Args:
        caminho_arquivo: caminho para o CSV
        
    Returns:
        DataFrame com os dados
    """

    df = pd.read_csv(caminho_arquivo)

    return df


def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print("=" * 50)
    print("EXPLORAÇÃO DOS DADOS")
    print("=" * 50)

    print(f"Shape: {df.shape}")

    print()
    print(df.dtypes)

    print()
    print(df.head())

    print("=" * 50)


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("\nDISTRIBUIÇÃO DO TARGET")
    print("-" * 30)

    print()
    print(df[coluna_target].value_counts())

    print()
    print(df[coluna_target].value_counts(normalize=True))

    print("-" * 30)


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("../data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
