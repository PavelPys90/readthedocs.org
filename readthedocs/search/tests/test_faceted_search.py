import pytest

from readthedocs.search.faceted_search import PageSearch


@pytest.mark.django_db
@pytest.mark.search
class TestPageSearch:
    @pytest.mark.parametrize("case", ["upper", "lower", "title"])
    def test_search_exact_match(self, client, project, case):
        """Check quoted query match exact phrase with case insensitively

        Making a query with quoted text like ``"foo bar"`` should match
        exactly ``foo bar`` or ``Foo Bar`` etc
        """
        # `Sphinx` word is present both in `kuma` and `docs` files
        # But the phrase `Sphinx uses` is available only in kuma docs.
        # So search with this phrase to check
        query_text = r'"Sphinx uses"'
        cased_query = getattr(query_text, case)
        query = cased_query()

        page_search = PageSearch(query=query)
        results = page_search.execute()

        assert len(results) == 2
        assert results[0]["project"] == "kuma"
        assert results[0]["path"] == "testdocumentation"
        assert results[0]["version"] == "stable"

        assert results[1]["project"] == "kuma"
        assert results[1]["path"] == "testdocumentation"
        assert results[1]["version"] == "latest"

    def test_search_combined_result(self, client, project):
        """Check search result are combined of both `AND` and `OR` operator

        If query is `Foo Bar` then the result should be as following order:

        - Where both `Foo Bar` is present
        - Where `Foo` or `Bar` is present
        """
        query = "Elasticsearch Query"
        page_search = PageSearch(query=query)
        results = page_search.execute()
        assert len(results) == 6

        result_paths_latest = [r.path for r in results if r.version == "latest"]
        result_paths_stable = [r.path for r in results if r.version == "stable"]
        # ``guides/wipe-environment`` page has both ``Elasticsearch Query`` words
        # ``docker`` page has ``Elasticsearch`` word
        # ``installation`` page has ``Query`` word.
        expected_paths = ["guides/wipe-environment", "docker", "installation"]

        assert result_paths_latest == expected_paths
        assert result_paths_stable == expected_paths
