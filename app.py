import streamlit as st
            "estado": estado,
            "status": status
        })

        st.success("Pedido cadastrado com sucesso!")

# VISUALIZAÇÃO
elif menu == "Visualizar Dados":
    st.subheader("Pedidos")

    dados = list(colecao.find())

    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df)
    else:
        st.warning("Nenhum dado encontrado.")

# EDIÇÃO
elif menu == "Editar Dados":
    st.subheader("Editar Pedido")

    cliente_busca = st.text_input("Cliente para editar")

    novo_status = st.selectbox(
        "Novo Status",
        ["Processando", "Enviado", "Entregue"]
    )

    if st.button("Atualizar"):
        colecao.update_many(
            {"cliente": cliente_busca},
            {"$set": {"status": novo_status}}
        )

        st.success("Pedido atualizado!")

# EXCLUSÃO
elif menu == "Excluir Dados":
    st.subheader("Excluir Pedido")

    cliente_delete = st.text_input("Cliente para excluir")

    if st.button("Excluir"):
        colecao.delete_many({"cliente": cliente_delete})
        st.success("Pedido removido!")

# DASHBOARD
elif menu == "Dashboard":
    st.subheader("Indicadores")

    dados = list(colecao.find())

    if dados:
        df = pd.DataFrame(dados)

        st.metric("Total de Pedidos", len(df))
        st.metric("Valor Médio", round(df["valor"].mean(), 2))

        grafico_estado = px.bar(
            df,
            x="estado",
            title="Pedidos por Estado"
        )

        st.plotly_chart(grafico_estado)

        grafico_categoria = px.pie(
            df,
            names="categoria",
            title="Categorias"
        )

        st.plotly_chart(grafico_categoria)

    else:
        st.warning("Sem dados para exibir.")