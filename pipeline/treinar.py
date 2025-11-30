"""
Pipeline - Etapa 3: Treinar Modelo
"""

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def preparar_dados(df, coluna_target='respondeu_campanha'):
    """
    Separa features (X) e target (y).
    
    Args:
        df: DataFrame completo
        coluna_target: nome da coluna target
        
    Returns:
        X (features), y (target)
    """

    X = df.drop(columns=[coluna_target, 'cliente_id'])
    y = df[coluna_target]

    return X, y


def dividir_treino_teste(X, y, tamanho_teste=0.2, random_state=42):
    """
    Divide os dados em treino e teste.
    
    Args:
        X: features
        y: target
        tamanho_teste: proporção para teste (0.2 = 20%)
        random_state: semente para reprodutibilidade
        
    Returns:
        X_train, X_test, y_train, y_test
    """

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=tamanho_teste, random_state=random_state)

    # Mostrar tamanhos
    if X_train is not None:
        print(f"Dados de treino: {len(X_train)} registros")
        print(f"Dados de teste: {len(X_test)} registros")

    return X_train, X_test, y_train, y_test


def treinar_modelo(X_train, y_train):
    """
    Treina um RandomForestClassifier.
    
    Args:
        X_train: features de treino
        y_train: target de treino
        
    Returns:
        Modelo treinado
    """

    print()
    print("Treinando modelo...")

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)  # Substitua None pelo código correto

    # Passo 2: Treinar o modelo (se foi criado)

    if modelo is not None:
        modelo.fit(X_train, y_train)

    print("✅ Modelo treinado!")
    return modelo


def salvar_modelo(modelo, caminho='models/modelo_campanha.pkl'):
    """
    Salva o modelo treinado em disco.
    
    Args:
        modelo: modelo treinado
        caminho: onde salvar
    """
    joblib.dump(modelo, caminho)
    print()
    print(f"Modelo salvo em: {caminho}")


# Teste local
if __name__ == "__main__":
    # Carregar dados
    df = pd.read_csv("../data/clientes_campanha.csv")

    # Preparar
    X, y = preparar_dados(df)

    if X is None or y is None:
        print("ERRO: Complete os TODOs 1 e 2!")
    else:
        # Dividir
        X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

        if X_train is None:
            print("ERRO: Complete o TODO 3!")
        else:
            # Treinar
            modelo = treinar_modelo(X_train, y_train)

            if modelo is None:
                print("ERRO: Complete os TODOs 4 e 5!")
            else:
                salvar_modelo(modelo)
